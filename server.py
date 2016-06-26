import spotipy, requests, os, json, grequests
from jinja2 import StrictUndefined
from pprint import pprint
from flask import Flask, render_template, redirect, request, flash, session, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime

# spotify_consumer_key = os.environ['SPOTIFY_CONSUMER_KEY']
# spotify_consumer_secret = os.environ['SPOTIFY_CONSUMER_SECRET']

# spotify = spotipy.Spotify()

app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def home():
    """Home page."""

    return render_template("home.html")

@app.route('/search')
def search():
    """Show search results for user not logged in."""

    return render_template("search_results.html")

@app.route('/logged_in_search')
def logged_in_search():
    """Show search results and dashboard for logged in user."""

    return render_template("logged_in_search.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
