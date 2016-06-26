from flask_wtf import Form
from wtforms import StringField, PasswordField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class SignUpForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('password_confirm', validators=[
        DataRequired(),
        Length(min=6),
        EqualTo('password', message='Passwords must match')
    ])


class SignInForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class PostForm(Form):
    id = HiddenField('id')
    text = TextAreaField('text', validators=[DataRequired()])
