"""Models and database functions for Company Website project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################


# Model definitions

class Brand(db.Model):
    """Brand of past/complete projects."""

    __tablename__ = "brands"

    brand_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    brand_name = db.Column(db.String(50), unique=True, nullable=False)
    website = db.Column(db.String(50), nullable=True)
    description_top = db.Column(db.Text, nullable=False)
    founded_yr = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(50), nullable=False)
    description_bottom = db.Column(db.Text, nullable=True)
    banner_img = db.Column(db.String(50), nullable=True)
    photo_a = db.Column(db.String(50), nullable=True)
    photo_b = db.Column(db.String(50), nullable=True)
    photo_c = db.Column(db.String(50), nullable=True)
    photo_d = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        """Representation when printed."""

        return "<Brand brand_id=%s brand_name=%s>" % (self.brand_id,
                                                      self.brand_name)

    #Define relationship products table
    products = db.relationship("Product",
                               backref=db.backref("brands"))


class Product(db.Model):
    """Product of brands."""

    __tablename__ = "products"

    product_id = db.Column(db.Integer,
                           autoincrement=True,
                           primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    size = db.Column(db.String(30), nullable=True)
    photo_y = db.Column(db.String(50), nullable=False)
    photo_z = db.Column(db.String(50), nullable=True)
    brand_id = db.Column(db.Integer,
                         db.ForeignKey('brands.brand_id'))

    def __repr__(self):
        """Representation when printed."""

        return "<Product product_id=%s product_name=%s>" % (self.product_id,
                                                            self.product_name)


class Project(db.Model):
    """Work in progress."""

    __tablename__ = "projects"

    project_id = db.Column(db.Integer,
                           autoincrement=True,
                           primary_key=True)
    project_name = db.Column(db.String(50), nullable=False)
    logo_img = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Representation when printed."""

        return "<Project project_id=%s project_name=%s>" % (self.project_id,
                                                            self.project_name)


#####   HELPER FUNCTIONS  ######################################################

def connect_to_db(app, db_uri='postgresql:///company'):
    """Connect the database to the Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

################################################################################

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print ("Connected to DB.")
