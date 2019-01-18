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
    """Homepage."""

    return render_template("index.html")


@app.route('/brands')
def show_projects():
    """List of past projects by brand."""

    return render_template("brands.html")


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
