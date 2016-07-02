from flask import Blueprint

blogging = Blueprint('blogging', __name__,
                     template_folder='templates')

from application.blogging import routes
