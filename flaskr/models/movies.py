"""sqlalchemy Movies class file"""
# pylint: disable=R0913, R0903, R0902
from typing import List
import datetime
from flaskr import db

movie_director = db.Table('movie_director',
                          db.Column('movie_id',
                                    db.Integer,
                                    db.ForeignKey('movies.movie_id',
                                                  onupdate="CASCADE",
                                                  ondelete="CASCADE")),
                          db.Column('director_id',
                                    db.Integer,
                                    db.ForeignKey('directors.director_id',
                                                  onupdate="CASCADE",
                                                  ondelete="CASCADE")))

movie_genre = db.Table("movie_genre",
                       db.Column('movie_id',
                                 db.Integer,
                                 db.ForeignKey('movies.movie_id',
                                               onupdate="CASCADE",
                                               ondelete="CASCADE")),
                       db.Column('genre_id',
                                 db.Integer,
                                 db.ForeignKey('genres.genre_id',
                                               onupdate="CASCADE",
                                               ondelete="CASCADE")),
                       )


class Movies(db.Model):
    """sqlalchemy Movies model"""
    __tablename__: str = 'movies'
    movie_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    release_date = db.Column(db.DateTime(timezone=True), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(500), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id',
                                                  onupdate="CASCADE",
                                                  ondelete="CASCADE"))
    directors = db.relationship("Directors",
                                secondary=movie_director,
                                backref=db.backref("movies", lazy="dynamic"))
    genres = db.relationship("Genres",
                             secondary=movie_genre,
                             backref=db.backref("movies", lazy="dynamic"))

    def __init__(self,
                 name: str,
                 release_date: datetime,
                 description: str,
                 rating: int,
                 poster_url: str,
                 user_id: int,
                 genres: List,
                 directors: List,
                 ) -> None:
        self.name = name
        self.release_date = release_date
        self.description = description
        self.rating = rating
        self.poster_url = poster_url
        self.user_id = user_id
        self.genres = genres
        self. directors = directors

    def __repr__(self) -> str:
        return f"<Movies:{self.movie_id}', {self.name}, {self.directors}>"
