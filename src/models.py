from src import db
from flask_login import UserMixin

class Admin(db.Model, UserMixin):
    """Admin Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)

class LinkModel(db.Model, UserMixin):
    """Model for the relationship between link and shortlink"""
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    shortlink = db.Column(db.String(40), nullable=False, unique=True)