from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.auth.forms import LoginForm
from src.models import Admin
from flask_login import login_user, logout_user

from src import db, bcrypt

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', "POST"])
def login():
    """Route for loggging in an admin"""
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password,
                                               form.password.data):
            login_user(admin, remember=True)
            next_page = request.args.get('next')
            print(next_page)
            return redirect(next_page if next_page else '/')

    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    """Signs out the current user."""
    logout_user()
    return redirect('/')