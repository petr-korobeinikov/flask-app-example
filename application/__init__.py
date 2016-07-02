import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('application.config.{}'.format(os.environ['APP_SETTINGS']))

db = SQLAlchemy(app)

from application.blogging import blogging

app.register_blueprint(blogging, url_prefix='/blog')

from application import auth
from application import routes
from application import errors
