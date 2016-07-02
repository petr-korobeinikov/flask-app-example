from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from application.models import Person
from application.util.wtforms_validation import UniqueField


class SignUpForm(Form):
    username = StringField('username', validators=[
        DataRequired(),
        UniqueField(model=Person)
    ])
    email = StringField('email', validators=[
        DataRequired(),
        Email(),
        UniqueField(model=Person)
    ])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('password_confirm', validators=[
        DataRequired(),
        Length(min=6),
        EqualTo('password', message='Passwords must match')
    ])


class SignInForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
