import os
from flask import Flask

app = Flask(__name__)
app.config.from_object('application.config.{}'.format(os.environ['APP_SETTINGS']))

from application import database
from application import auth
from application import routes
from application import errors
