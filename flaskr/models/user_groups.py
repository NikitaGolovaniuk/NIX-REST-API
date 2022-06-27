"""sqlalchemy UserGroups class file"""
# pylint: disable=R0913, R0903
from flaskr import db


class UserGroups(db.Model):
    """sqlalchemy Movies model"""
    __tablename__: str = 'user_groups'
    user_group_id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'<UserGroups:{self.name}>'
