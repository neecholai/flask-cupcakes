"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_image = 'https://tinyurl.com/demo-cupcake'


def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """"Create cupcake model / table"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(80), nullable=False)
    size = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float(1), nullable=False)
    image = db.Column(db.Text, nullable=False,
                      default=default_image)
