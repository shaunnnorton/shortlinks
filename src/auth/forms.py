from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Label
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Form for logging in"""
    label = Label("Login","Admin Login \n")
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Log In")