from application import app, db
from application.models import Person, Post
from application.forms import SignInForm, SignUpForm, PostForm
from flask import templating, redirect, url_for, flash, abort, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_paginate import Pagination
from sqlalchemy import func


@app.route('/')
def index():
    return templating.render_template('index.j2')


@app.route('/posts/')
def post_index():
    per_page = 3

    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    count = db.session.query(func.count(Post.id)).scalar()
    posts = db.session.query(Post).order_by(Post.id).limit(per_page).offset(page * per_page - per_page)

    pagination = Pagination(page=page, total=count, per_page=per_page)
    return templating.render_template('post_index.j2', posts=posts, pagination=pagination)


@app.route('/posts/<int:post_id>')
def post_show(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        abort(404)
    return templating.render_template('post_show.j2', post=post)


@app.route('/posts/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_edit(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if post is None:
        abort(404)

    if post.person_id != current_user.id:
        abort(403)

    form = PostForm(request.form, obj=post)
    if request.method == 'POST' and form.validate():
        post.text = form.text.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post_show', post_id=post_id))

    return templating.render_template('post_edit.j2', form=form, post_id=post_id)


@app.route('/posts/new', methods=['GET', 'POST'])
@login_required
def post_new():
    post = Post()
    form = PostForm(request.form, obj=post)
    if request.method == 'POST' and form.validate():
        post.text = form.text.data
        post.person_id = current_user.id
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post_show', post_id=post.id))

    return templating.render_template('post_new.j2', form=form)


@app.route('/posts/delete/<int:post_id>')
def post_delete(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if post is None:
        abort(404)

    if post.person_id != current_user.id:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('post_index'))


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
