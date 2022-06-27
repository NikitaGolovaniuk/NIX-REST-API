"""sqlalchemy Directors class file"""
# pylint: disable=R0913, R0903, E0401
from flaskr.db import db


class Directors(db.Model):
    """sqlalchemy Directors model"""
    __tablename__: str = 'directors'
    director_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"<Director {self.name}>"
