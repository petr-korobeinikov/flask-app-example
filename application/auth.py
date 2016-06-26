from application import app
from application.models import Person
from flask import redirect, url_for
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_person(person_id):
    person = Person.query.filter(Person.id == person_id).first()
    return person


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('signin'))
