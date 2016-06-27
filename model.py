"""Models and database functions for Tortola."""

from flask_sqlalchemy import SQLAlchemy



# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class User(db.Model):
    """A user can save multiple events."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Event user_id=%s user_name =%s>" % (self.user_id,
                                                 self.user_name)



def connect_to_db(app, db_uri="postgresql:///tortoladb"):
    """Connect the database to our Flask app."""

    # Configure to use our postgres database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."