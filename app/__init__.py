import os
import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = psycopg2.connect(host='localhost', dbname='game_of_guessing', user='postgres', password='sh@rpn3ltoor')
db.autocommit = False
cursor = db.cursor()
db = SQLAlchemy(app)

from app import routes
