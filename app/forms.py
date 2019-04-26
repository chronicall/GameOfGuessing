import re

from app import cursor

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, BooleanField, SubmitField, FormField, SelectField
from wtforms.form import BaseForm
from wtforms.validators import InputRequired, ValidationError


class Email(object):

    def __call__(self, form, field):
        ## Get email address rules to make sure regex is correct
        ## Maybe add re.I flag for case-insensitive matching, allowing:
        ##      - SANDRA@SENSA.IS
        ##      - sandra@SENSA.is
        ##      - SANDRA@sensa.is
        ##      - sAnDrA@SeNsA.iS
        ##      - etc.
        mail_matcher = re.match(r'^[a-zA-Z]+@sensa.is$', field.data)
        if not mail_matcher:
            raise ValidationError('{} is not a valid @sensa.is email address'.format(field.data))
        
        ## Check if actually associated with an employee??
        ## is this too much for this project?

        ## Check if already in database
        mail = mail_matcher.group()
        cursor.execute("""SELECT email FROM person WHERE email = %s""", (mail,))
        exists = cursor.fetchone()
        if exists:
            raise ValidationError('Email {} already exists in the database. Please enter just once :c'.format(mail_matcher.group()))


class QuestionForm(FlaskForm):

    name = StringField('Name', validators=[InputRequired('Need to know your name.')])
    email = StringField('Email', validators=[InputRequired('Please enter your email.'), Email()])
    
    #### Questions begin
    alive_or_dead = [('Alive', ''), ('Dead', '')]
    jon_snow = RadioField(
            'Jon Snow',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    jon_snow_ww = BooleanField('')

    sansa_stark = RadioField(
            'Sansa Stark',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    sansa_stark_ww = BooleanField('')

    arya_stark = RadioField(
            'Arya Stark',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    arya_stark_ww = BooleanField('')

    bran_stark = RadioField(
            'Bran Stark',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    bran_stark_ww = BooleanField('')

    cersei_lannister = RadioField(
            'Cersei Lannister',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    cersei_lannister_ww = BooleanField('')

    jamie_lannister = RadioField(
            'Jamie Lannister',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    jamie_lannister_ww = BooleanField('')

    tyrion_lannister = RadioField(
            'Tyrion Lannister',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    tyrion_lannister_ww = BooleanField('')

    daenerys_targaryen = RadioField(
            'Daenerys Targaryen',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    daenerys_targaryen_ww = BooleanField('')

    theon_greyjoy = RadioField(
            'Theon Greyjoy',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    theon_greyjoy_ww = BooleanField('')

    yara_greyjoy = RadioField(
            'Yara Greyjoy',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    yara_greyjoy_ww = BooleanField('')

    melisandre = RadioField(
            'Melisandre',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    melisandre_ww = BooleanField('')

    jorah_mormont = RadioField(
            'Jorah Mormont',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    jorah_mormont_ww = BooleanField('')

    the_hound = RadioField(
            'The Hound',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    the_hound_ww = BooleanField('')

    the_mountain = RadioField(
            'The Mountain',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    the_mountain_ww = BooleanField('')

    samwell_tarly = RadioField(
            'Samwell Tarly',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    samwell_tarly_ww = BooleanField('')

    gilly = RadioField(
            'Gilly',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    gilly_ww = BooleanField('')

    sam_jr = RadioField(
            'Sam Jr.',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    sam_jr_ww = BooleanField('')

    lord_varys = RadioField(
            'Lord Varys',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    lord_varys_ww = BooleanField('')

    brienne_of_tarth = RadioField(
            'Brienne of Tarth',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    brienne_of_tarth_ww = BooleanField('')

    davos_seaworth = RadioField(
            'Davos Seaworth',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    davos_seaworth_ww = BooleanField('')

    bronn = RadioField(
            'Bronn',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    bronn_ww = BooleanField('')

    podrick_payne = RadioField(
            'Podrick Payne',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    podrick_payne_ww = BooleanField('')

    tormund_giantsbane = RadioField(
            'Tormund Giantsbane',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    tormund_giantsbane_ww = BooleanField('')

    greyworm = RadioField(
            'Greyworm',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    greyworm_ww = BooleanField('')

    gendry = RadioField(
            'Gendry',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    gendry_ww = BooleanField('')

    beric_dondarrion = RadioField(
            'Beric Dondarrion',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    beric_dondarrion_ww = BooleanField('')

    euron_greyjoy = RadioField(
            'Euron Greyjoy',
            choices=alive_or_dead,
            validators=[InputRequired('Please select one option.')]
    )
    euron_greyjoy_ww = BooleanField('')
    #### Questions end

    #### Bonus start
    select_choices = [('Yes', 'Yes'), ('No', 'No')]
    daenerys_pregnant = SelectField(
            'Is Daenerys pregnant?',
            choices=select_choices
    )
    #BooleanField('Is Daenerys pregnant?')
    #StringField('Is Daenerys pregnant?', validators=[])
    brienne_x_tormund = SelectField(
            'Will Brienne and Tormund get together?',
            choices=select_choices
    )
    #BooleanField('Will Brienne and Tormund get together?')
    #StringField('Will Brienne and Tormund get together?', validators=[])
    night_king_death = StringField('Who fells the Nightking?')
    night_king_death_by = StringField('What (weapon/thing) fells the Nightking?')
    iron_throne = StringField('Who sits in the Iron Throne in the end?')
    #### Bonus end

    submit = SubmitField('Send')
