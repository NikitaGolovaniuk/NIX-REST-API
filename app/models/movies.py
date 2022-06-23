from app import db

movie_director = db.Table('movie_director',
                          db.Column('movie_id', db.Integer, db.ForeignKey('movies.movie_id')),
                          db.Column('director_id', db.Integer, db.ForeignKey('directors.director_id')))

movie_genre = db.Table("movie_genre",
                       db.Column('movie_id', db.Integer, db.ForeignKey('movies.movie_id')),
                       db.Column('genre_id', db.Integer, db.ForeignKey('genres.genre_id')),
                       )


class Movies(db.Model):
    __tablename__ = 'movies'
    movie_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    release_date = db.Column(db.DateTime(timezone=True), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(500), nullable=True)
    directors = db.relationship("Directors", secondary=movie_director, backref=db.backref("movies", lazy="dynamic"))
    genres = db.relationship("Genres", secondary=movie_genre, backref=db.backref("movies", lazy="dynamic"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f"<Movies:{self.movie_id}', {self.name}, {self.directors}>"
