from app.db import db


class Directors(db.Model):
    __tablename__ = 'directors'
    director_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Director %r>' % self.name

