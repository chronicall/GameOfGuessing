create table person (
    id serial primary key,
    name text not null,
    score int not null,
    email text unique not null
);

create table question (
    id serial primary key,
    question text not null,
    answer text null
);

create table guess (
    id serial primary key,
    question_id int not null references question(id),
    person_id int not null references person(id)
);

create table base_guess (
    id serial primary key,
    guess boolean not null,
    whitewalker boolean not null,
    guess_id int not null references guess(id)
);

create table bonus_guess (
    id serial primary key,
    guess text not null,
    guess_id int not null references guess(id)
);

-- TODO: Create procedures for queries used a lot?
-- TODO: Create triggers to update score for people when an answer gets entered.
