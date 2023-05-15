from flask import redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Label, URLField
from wtforms.validators import DataRequired, URL, Length


class GenerateForm(FlaskForm):
    """Form to generate a new shortlink redirect."""
    label = Label("label", "Create Shortlink")
    url = URLField("URL",validators=[DataRequired(),URL()])
    shortlink = StringField("Shortlink", validators=[Length(min=4,max=40), DataRequired()])
    submit = SubmitField("Create Shortlink")


class ModifyForm(FlaskForm):
    """Form to modify a new shortlink"""
    label = Label("label","Modify Shortlink")
    url = URLField("URL",validators=[DataRequired(),URL()])
    shortlink = StringField("Shortlink", validators=[Length(min=4,max=40), DataRequired()])
    submit = SubmitField("Modify Shortlink")