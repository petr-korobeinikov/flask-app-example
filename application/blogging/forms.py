from flask.ext.wtf import Form
from wtforms import HiddenField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(Form):
    id = HiddenField('id')
    text = TextAreaField('text', validators=[DataRequired()])
