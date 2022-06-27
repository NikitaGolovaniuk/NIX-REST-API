"""sqlalchemy Genres class file"""
# pylint: disable=R0913, R0903
from flaskr import db


class Genres(db.Model):
    """sqlalchemy Genres model"""
    __tablename__: str = 'genres'
    genre_id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return "<Genre {self.name}>"
