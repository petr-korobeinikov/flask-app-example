from application import app, db
from application.models import Person
from application.forms import SignInForm, SignUpForm
from flask import templating, redirect, url_for, flash, abort, request
from flask_login import login_user, logout_user, current_user
from flask_paginate import Pagination
from sqlalchemy import func


@app.route('/')
def index():
    return templating.render_template('index.j2')


@app.route('/people')
def person_index():
    per_page = 3

    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    count = db.session.query(func.count(Person.id)).scalar()
    people = db.session.query(Person).order_by(Person.id).limit(per_page).offset(page * per_page - per_page)

    pagination = Pagination(page=page, total=count, per_page=per_page)
    return templating.render_template('person_index.j2', people=people, pagination=pagination)


@app.route('/me')
@app.route('/people/<int:person_id>')
def person_show(person_id=None):
    if person_id is None:
        if current_user.is_authenticated:
            person_id = current_user.id
        else:
            abort(403)

    person = Person.query.filter_by(id=person_id).first()

    if person is None:
        abort(404)

    return templating.render_template('person_show.j2', person=person)


@app.route('/signup', methods=['GET', 'POST'])
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


@app.route('/signin', methods=['GET', 'POST'])
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


@app.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('index'))
