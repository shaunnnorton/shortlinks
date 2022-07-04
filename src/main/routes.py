from gc import freeze
from logging import exception
from flask import Blueprint, render_template, redirect, request, url_for, flash
import flask
from flask_login import login_required

from src import app , db
from src.models import LinkModel
from .forms import GenerateForm
from src.utils.utils import validate_redirect, remove_relation

main = Blueprint("main", __name__)

@main.route("/")
def default_redirect():
    return redirect(url_for("main.Gen_route"))

@main.route("/Gen")
def Gen_route():
    form=GenerateForm()
    
    return render_template("gen.html",form=form)

@main.route("/n/<shorthand>")
def redirect_function(shorthand):
    try:
        link = LinkModel.query.filter_by(shortlink=shorthand).first()
        print(link)
        return redirect(link.original_url)
    except AttributeError:
        flash(f"OPPS it looks like we dont have a redirect for \"{shorthand}\"")
        return redirect(url_for("main.Gen_route"))
    except:
        flash("Something Went Wrong")
        return redirect(url_for("main.Gen_route"))


@main.route("/Admin")
@login_required
def Admin_route():
    all_records = LinkModel.query.all()
    
    
    return render_template('admin.html', records=all_records)

@main.route("/Gen/CreateShortlink", methods=["POST"])
def CreateShortlink():
    try:
        original_url = request.form.get("url")
        shortlink = request.form.get("shortlink")  
        if validate_redirect(original_url)[0] == False:
            raise Exception("Provided URL did not return a vaild Status code")
        new_shortlink = LinkModel(
            original_url=original_url,
            shortlink=shortlink
        )
        db.session.add(new_shortlink)
        db.session.commit()
        flash("Success")
        return redirect(url_for('main.redirect_function',shorthand=new_shortlink.shortlink))
    except Exception as e:
        print(e)
        db.session.rollback()
        flash("Error creating shortlink. Try using different text for your shortlink.")
        return redirect(url_for('main.Gen_route'))

@main.route("/Admin/remove", methods=["POST"])
@login_required
def remove_route():
    print(request.form)
    keys = request.form.keys()
    for key in keys:
        remove_relation(key)    
    flash(f"Deleted {keys}")
    return redirect(url_for("main.Admin_route"))