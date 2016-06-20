from application import app, db
from application.forms import SignInForm, SignUpForm
from flask import templating, redirect, url_for


@app.route('/')
def index():
    now, name = db.engine.execute("select now(), 'flask'").fetchone()
    return templating.render_template('index.j2', now=now, name=name)


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
        pass

    return templating.render_template('signin.j2', form=form)


@app.route('/signout')
def signout():
    return redirect(url_for('index'))
