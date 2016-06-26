import spotipy, requests, os, json, grequests
from jinja2 import StrictUndefined
from pprint import pprint
from flask import Flask, render_template, redirect, request, flash, session, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime

spotify_consumer_key = os.environ['SPOTIFY_CONSUMER_KEY']
spotify_consumer_secret = os.environ['SPOTIFY_CONSUMER_SECRET']
bandsintown_app_id = os.environ['BANDSINTOWN_ID']

spotify = spotipy.Spotify()

app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

def get_events_for_artist_and_city(artist, city):

    event_request = 'http://api.bandsintown.com/events/search?artists[]='+artist+'&location='+city+'&radius=10&format=json&app_id='+bandsintown_app_id
    event_request = requests.get(event_request)
    jdict_events = event_request.json()
    pprint(jdict_events)

def get_artist_spotify_uri(artist):
    """Search for artist in database, if not there, get Spotify URI and save artist to db."""

    #update this once you have set up the model.py --> see events project for code

    artist_search = spotify.search(artist, limit=1, offset=0, type='artist')

    if artist_search['artists']['items'] == []:
        print artist_search['artists']['items']
        return None

    else:
        artist_uri = artist_search['artists']['items'][0]['uri'].lstrip("spotify:artist:")

    return artist_uri


def get_artist_spotify_img(artist):
    """Get an artist's image from Spotify."""

    results = spotify.search(q='artist:' + artist, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist_lu = items[0]
        artist_img = artist_lu['images'][0]['url']
    else:
        artist_img = 'https://pbs.twimg.com/profile_images/1324123785/macaroni_noodle_icom_-_web_taken_400x400.jpg'

    return artist_img


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
