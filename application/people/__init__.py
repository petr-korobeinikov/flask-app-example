from flask import Blueprint

people = Blueprint('people', __name__,
                   template_folder='templates')

from application.people import routes
