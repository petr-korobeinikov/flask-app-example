import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../static')
app.config.from_object('application.config.{}'.format(os.environ['APP_SETTINGS']))

db = SQLAlchemy(app)

from application.blogging import blogging
from application.auth import auth

app.register_blueprint(blogging, url_prefix='/blog')
app.register_blueprint(auth)

from application import routes
from application import errors
