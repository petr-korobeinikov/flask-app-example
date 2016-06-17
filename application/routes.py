from application import app, db
from flask import templating


@app.route('/')
def index():
    now, name = db.engine.execute("select now(), 'flask'").fetchone()
    return templating.render_template('index.j2', now=now, name=name)
