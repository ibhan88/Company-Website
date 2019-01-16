"""Models and database functions for Company Website project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################


# Model definitions



#####   HELPER FUNCTIONS  ######################################################

def connect_to_db(app, db_uri='postgresql:///company'):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

################################################################################

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
