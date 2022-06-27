"""sqlalchemy Users class file"""
# pylint: disable=R0913, R0903, E0401
from flask_login import UserMixin
from flaskr.models.user_groups import UserGroups
from flaskr import db


class Users(db.Model, UserMixin):
    """sqlalchemy Users model"""
    __tablename__: str = 'users'
    user_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(500), unique=True, nullable=False)
    user_group_id = db.Column(db.Integer, db.ForeignKey('user_groups.user_group_id',
                                                        onupdate="CASCADE",
                                                        ondelete="CASCADE"))

    def __init__(self,
                 name: str,
                 password: str,
                 username: str,
                 user_group_id: int) -> None:
        self.name = name
        self.password = password
        self.username = username
        self.user_group_id = user_group_id

    def is_admin(self):
        """check is user admin"""
        role = UserGroups.query.filter_by(user_group_id=self.user_group_id).first().name

        if role != "admin":
            return False

        return True

    def __repr__(self) -> str:
        return f'<User:{self.username}{self.password}{self.user_group_id}>'
