from app import db


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_group_id = db.Column(db.Integer, db.ForeignKey('user_groups.user_group_id'))

    def __repr__(self):
        return f'<User:{self.name}{self.password}{self.user_group_id}>'
