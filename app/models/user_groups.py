from app import db


class UserGroups(db.Model):
    __tablename__ = 'user_groups'
    user_group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

