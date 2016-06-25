from application import app, db
from application.models import Person, Post
from application.forms import SignInForm, SignUpForm
from flask import templating, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required


@app.route('/')
def index():
    return templating.render_template('index.j2')


@app.route('/posts/')
def posts():
    posts = db.session.query(Post).all()
    return templating.render_template('post_index.j2', posts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        pass

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
