from app import app, cursor
from app.forms import QuestionForm
from app.psql_support import insert_person_and_guesses

from flask import render_template, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
@app.route('/Home', methods=['GET', 'POST'])
def home():
    form = QuestionForm()
    if form.validate_on_submit():
        try:
            new_id = insert_person_and_guesses(cursor, form)
            return redirect(url_for('person', id_=new_id))
        except Exception as e:
            return (str(e))
    return render_template('index.html', title='Game of Guessing', form=form)

@app.route('/Leaderboard')
def leaderboard():
    try:
        cursor.execute(
            """SELECT id, name, score, email
               FROM person
            """
        )
        persons = cursor.fetchall()
        ## Sort by score
        persons = sorted(persons, key=lambda x: x[2], reverse=True)
        
        return render_template('leaderboard.html', persons=persons)
    except Exception as e:
        return (str(e))

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Person/<id_>')
def person(id_):
    try:
        cursor.execute(
            """SELECT name, score, email 
               FROM person
               WHERE id = %s
            """,
            (id_,)
        )
        person = cursor.fetchone()
        ### Get guesses for questions.
        cursor.execute(
            """SELECT question.question, base.guess, base.whitewalker
               FROM base_guess base
               INNER JOIN guess ON base.guess_id = guess.id
               INNER JOIN question ON guess.question_id = question.id
               WHERE guess.person_id = %s
            """,
            (id_,)
        )
        base_guesses = cursor.fetchall()

        cursor.execute(
            """SELECT question.question, bonus.guess 
               FROM bonus_guess bonus
               INNER JOIN guess ON bonus.guess_id = guess.id 
               INNER JOIN question ON guess.question_id = question.id
               WHERE guess.person_id = %s
            """,
            (id_,)
        )
        bonus_guesses = cursor.fetchall()

        return render_template(
            'person.html',
            person=person,
            base_guesses=base_guesses,
            bonus_guesses=bonus_guesses
        )
    except Exception as e:
        return (str(e))
