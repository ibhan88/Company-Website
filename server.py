"""Company Website"""

import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, flash, session, request
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db
import json
# from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Landing page."""

    return render_template("landing.html")


@app.route('/home')
def homepage():
    """Homepage."""

    return render_template("index.html")


@app.route('/admin')
def login_form():
    """Show admin login form."""

    if not session.get("user_id"):
        return render_template("admin.html")


@app.route('/admin', methods=['POST'])
def login_process():
    """Login the admin."""

    if not session.get("user_id"):
        username = request.form.get("username")
        password = request.form.get("password").encode('utf-8')

        user = User.query.filter_by(username=username).first()

        if not user:
            flash("No such user exists")
            return redirect("/login")

        if not bcrypt.checkpw(password, user.password.encode('utf-8')):
            flash("Incorrect password")
            return redirect("/login")

        session["user_id"] = user.user_id
        session["username"] = user.username

        flash("Logged in")

    return redirect("/")


@app.route('/works')
def show_projects():
    """List of works by brand."""

    return render_template("works.html")


@app.route('/upcoming')
def show_upcoming_projects():
    """List of works in progress."""

    return render_template("upcoming.html")


@app.route('/misc')
def show_misc_projects():
    """List of miscellaneous projects."""

    return render_template("misc.html")


@app.route('/about')
def show_about_us():
    """Description of company."""

    return render_template("about.html")


@app.route('/contact')
def show_contact():
    """Contact information and form."""

    return render_template("contact.html")


@app.route('/submit', methods=["POST"])
def submit_contact_form():
    """Submit contact form."""

    return render_template("submit.html")


######### HELPER FUNCTIONS ####################################################

###############################################################################
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()
