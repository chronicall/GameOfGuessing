def insert_person_and_guesses(cursor, form):
    cursor.execute("""BEGIN""")
    ##################
    #### Person
    ##################
    cursor.execute(
        """INSERT INTO person (name, score, email)
           VALUES (%s, 0, %s)
           RETURNING id;
        """,
        (form.data['name'], form.data['email'],)
    )
    new_id = cursor.fetchone()[0]

    ##################
    #### Base guesses
    ##################
    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (1, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['jon_snow'] == 'Alive' else False,
            True if form.data['jon_snow_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (2, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['sansa_stark'] == 'Alive' else False,
            True if form.data['sansa_stark_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (3, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['arya_stark'] == 'Alive' else False,
            True if form.data['arya_stark_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (4, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['bran_stark'] == 'Alive' else False,
            True if form.data['bran_stark_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (5, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['cersei_lannister'] == 'Alive' else False,
            True if form.data['cersei_lannister_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (6, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['jamie_lannister'] == 'Alive' else False,
            True if form.data['jamie_lannister_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (7, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['tyrion_lannister'] == 'Alive' else False,
            True if form.data['tyrion_lannister_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (8, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['daenerys_targaryen'] == 'Alive' else False,
            True if form.data['daenerys_targaryen_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (9, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['theon_greyjoy'] == 'Alive' else False,
            True if form.data['theon_greyjoy_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (10, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['yara_greyjoy'] == 'Alive' else False,
            True if form.data['yara_greyjoy_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (11, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['melisandre'] == 'Alive' else False,
            True if form.data['melisandre_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (12, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['jorah_mormont'] == 'Alive' else False,
            True if form.data['jorah_mormont_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (13, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['the_hound'] == 'Alive' else False,
            True if form.data['the_hound_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (14, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['the_mountain'] == 'Alive' else False,
            True if form.data['the_mountain_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (15, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['samwell_tarly'] == 'Alive' else False,
            True if form.data['samwell_tarly_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (16, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['gilly'] == 'Alive' else False,
            True if form.data['gilly_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (17, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['sam_jr'] == 'Alive' else False,
            True if form.data['sam_jr_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (18, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['lord_varys'] == 'Alive' else False,
            True if form.data['lord_varys_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (19, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['brienne_of_tarth'] == 'Alive' else False,
            True if form.data['brienne_of_tarth_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (20, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['davos_seaworth'] == 'Alive' else False,
            True if form.data['davos_seaworth_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (21, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['bronn'] == 'Alive' else False,
            True if form.data['bronn_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (22, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['podrick_payne'] == 'Alive' else False,
            True if form.data['podrick_payne_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (23, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['tormund_giantsbane'] == 'Alive' else False,
            True if form.data['tormund_giantsbane_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (24, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['greyworm'] == 'Alive' else False,
            True if form.data['greyworm_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (25, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['gendry'] == 'Alive' else False,
            True if form.data['gendry_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (26, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['beric_dondarrion'] == 'Alive' else False,
            True if form.data['beric_dondarrion_ww'] else False,
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (27, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO base_guess (guess, whitewalker, guess_id)
           VALUES (%s, %s, %s);
        """,
        (
            True if form.data['euron_greyjoy'] == 'Alive' else False,
            True if form.data['euron_greyjoy_ww'] else False,
            guess_id,
        )
    )
    ##################
    #### Bonus guesses
    ##################
    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (28, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO bonus_guess (guess, guess_id)
           VALUES (%s, %s)
        """,
        (
            form.data['daenerys_pregnant'],
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (29, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO bonus_guess (guess, guess_id)
           VALUES (%s, %s)
        """,
        (
            form.data['brienne_x_tormund'],
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (30, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO bonus_guess (guess, guess_id)
           VALUES (%s, %s)
        """,
        (
            form.data['night_king_death'],
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (31, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO bonus_guess (guess, guess_id)
           VALUES (%s, %s)
        """,
        (
            form.data['night_king_death_by'],
            guess_id,
        )
    )

    cursor.execute(
        """INSERT INTO guess(question_id, person_id)
           VALUES (32, %s)
           RETURNING id;
        """,
        (new_id,)
    )
    guess_id = cursor.fetchone()[0]
    cursor.execute(
        """INSERT INTO bonus_guess (guess, guess_id)
           VALUES (%s, %s)
        """,
        (
            form.data['iron_throne'],
            guess_id,
        )
    )
    cursor.execute("""COMMIT""")

    return new_id
