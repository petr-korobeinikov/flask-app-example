import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('application.config.{}'.format(os.environ['APP_SETTINGS']))

db = SQLAlchemy(app)

from application import auth
from application import routes
