from app import db


class Genres(db.Model):
    __tablename__ = 'genres'
    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Genre %r>' % self.name
