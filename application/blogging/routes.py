from application.blogging import blogging
from application import db
from application.blogging.models import Post
from application.blogging.forms import PostForm
from flask import templating, redirect, url_for, abort, request
from flask_login import login_required, current_user
from flask_paginate import Pagination
from sqlalchemy import func


@blogging.route('/posts/')
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


@blogging.route('/posts/<int:post_id>')
def post_show(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        abort(404)
    return templating.render_template('post_show.j2', post=post)


@blogging.route('/posts/edit/<int:post_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('blogging.post_show', post_id=post_id))

    return templating.render_template('post_edit.j2', form=form, post_id=post_id)


@blogging.route('/posts/new', methods=['GET', 'POST'])
@login_required
def post_new():
    post = Post()
    form = PostForm(request.form, obj=post)
    if request.method == 'POST' and form.validate():
        post.text = form.text.data
        post.person_id = current_user.id
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blogging.post_show', post_id=post.id))

    return templating.render_template('post_new.j2', form=form)


@blogging.route('/posts/delete/<int:post_id>')
def post_delete(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if post is None:
        abort(404)

    if post.person_id != current_user.id:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blogging.post_index'))
