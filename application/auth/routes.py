from application.auth import auth
from application.auth.forms import SignInForm, SignUpForm
from application import db
from application.people.models import Person
from flask import templating, redirect, url_for, flash
from flask_login import login_user, logout_user


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        person = Person()
        person.username = form.username.data
        person.email = form.email.data
        person.password = form.password.data

        db.session.add(person)
        db.session.commit()

        login_user(person, remember=True)
        return redirect(url_for('index'))

    return templating.render_template('signup.j2', form=form)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()

    if form.validate_on_submit():
        person = Person.query.filter_by(username=form.username.data).first()
        if not person:
            flash('No such user.')

        if person and form.password.data == person.password:
            login_user(person, remember=True)
            return redirect(url_for('index'))

    return templating.render_template('signin.j2', form=form)


@auth.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('index'))
