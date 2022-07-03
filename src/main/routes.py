from flask import Blueprint, render_template, redirect, request, url_for, flash, blueprints

from src import app #, db

main = Blueprint("main", __name__)

@main.route("/")
def default_redirect():
    return redirect(url_for("main.Gen_route"))

@main.route("/Gen")
def Gen_route():
    return "In Develpoment"

@main.route("/<shorthand>")
def redirect_function(shorthand):
    return f"In Development: {shorthand}"

@main.route("/Admin")
def Admin_route():
    return f"In Development"
