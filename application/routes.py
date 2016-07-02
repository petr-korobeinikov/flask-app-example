from application import app
from flask import templating


@app.route('/')
def index():
    return templating.render_template('index.j2')
