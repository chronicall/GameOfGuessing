create or replace function update_score()
returns trigger
as $$
    declare
        t_curs cursor for
            select * from person;
        t_row person%rowtype;
        base_answer boolean;
        ww boolean;
        bonus_answer text;
        score_modifier integer;
    begin
        for t_row in t_curs loop
            score_modifier := 0;
            -- Skipping Theon and what weapon kills the Night King
            if old.id = 9 or old.id = 31 then
                continue;
            end if;
            -- Only do this if this is a new answer.
            if old.answer is NULL then
                -- Base questions; who lives and who dies and do they turn into a white walker?
                if old.id < 28 then
                    select b.guess, b.whitewalker into base_answer, ww
                    from base_guess b
                    inner join guess on b.guess_id = guess.id
                    inner join question on guess.question_id = question.id
                    inner join person on guess.person_id = t_row.id
                    where question.id = old.id;

                    if base_answer = true and ww = true then
                        continue;
                    end if;
                    
                    -- Possible answers:
                    --  dead && not whitewalker  = 0
                    --  dead && whitewalker      = 1
                    --  alive && not whitewalker = 2
                    --  any other combination is not considered as these would not be valid answers.

                    -- Character alive or dead?
                    if (base_answer = true and new.answer = '2') or (base_answer = false and (new.answer = '0' or new.answer = '1')) then
                        score_modifier := score_modifier + 1;
                    elsif (base_answer = true and new.answer != '2') or (base_answer = false and new.answer = '2') then
                        score_modifier := score_modifier - 1;
                    end if;

                    -- Character turned to whitewalker?
                    if (base_answer = false) and ((ww = true and new.answer = '1') or (ww = false and new.answer = '0')) then
                        score_modifier := score_modifier + 1;
                    elsif (base_answer = false) and (ww = false and new.answer = '1') then
                        score_modifier := score_modifier - 1;
                    end if;
                -- Bonus questions
                else
                    select b.guess into bonus_answer
                    from bonus_guess b
                    inner join guess on b.guess_id = guess.id
                    inner join question on guess.question_id = question.id
                    inner join person on guess.person_id = t_row.id
                    where question.id = old.id;
                    if old.id = 28 then
                        -- First bonus: Is Daenerys pregnant? 1 bonus point.
                        if bonus_answer = 'Yes' and new.answer = 'Yes' or bonus_answer = 'No' and new.answer = 'No' then
                            score_modifier := score_modifier + 1;
                        end if;
                    elsif old.id = 29 then
                        -- Second bonus: Will Brienne and Tormund get together? 1 bonus point.
                        if bonus_answer = 'Yes' and new.answer = 'Yes' or bonus_answer = 'No' and new.answer = 'No' then
                            score_modifier := score_modifier + 1;
                        end if;
                    elsif old.id = 30 then
                        -- Third bonus: Who kills the Night King? 2 bonus points.
                        if bonus_answer = new.answer then
                            score_modifier := score_modifier + 2;
                        end if;
                    elsif old.id = 31 then
                        -- Fourth bonus: What fells the Night King? 3 bonus points.
                        if bonus_answer = new.answer then
                            score_modifier := score_modifier + 3;
                        end if;
                    elsif old.id = 32 then
                        -- Fifth bonus: Who sits in the Iron Throne in the end? 4 bonus points.
                        if bonus_answer = new.answer then
                            score_modifier := score_modifier + 4;
                        end if;
                    end if;
                end if;
                update person
                    set score = score + score_modifier
                    where current of t_curs;
            else
                -- Handle updated answers.
            end if;
        end loop;
        return new;
    end;
$$ 
language plpgsql;

drop trigger if exists score_trigger on question;
create trigger score_trigger 
    after update on question 
    for each row
    execute procedure update_score();
