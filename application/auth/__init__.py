from flask import Blueprint, redirect, url_for
from flask_login import LoginManager
from application import app
from application.models import Person

auth = Blueprint('auth', __name__,
                 template_folder='templates')

from application.auth import routes

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_person(person_id):
    person = Person.query.filter(Person.id == person_id).first()
    return person


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.signin'))
