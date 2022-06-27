"""file with movie repository"""
# pylint: disable=R0913, R0903, E0401
from typing import Dict, Optional
from flaskr.crud.base_repo import BaseRepository
from flaskr.schemas.movies import MoviesSchema
from flaskr.models.movies import Movies
from flaskr.models.genres import Genres
from flaskr.models.directors import Directors
from flaskr.db import db


class MovieRepo(BaseRepository):
    """movie repository class"""
    def read(self, movie_id):
        """read method"""
        page_db_result = Movies.query.filter_by(movie_id=movie_id).all()
        if page_db_result:
            result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500

    def create(self, movie_schema: MoviesSchema):
        """create method"""
        try:
            tmp_genres_list = [Genres(name=i.name) for i in movie_schema.genres]
            tmp_directors_list = [Directors(name=i.name) for i in movie_schema.directors]
            db_obj = Movies(name=movie_schema.name,
                            rating=movie_schema.rating,
                            release_date=movie_schema.release_date,
                            description=movie_schema.description,
                            poster_url=movie_schema.poster_url,
                            user_id=movie_schema.user_id,
                            genres=tmp_genres_list,
                            directors=tmp_directors_list,
                            )
            db.session.add(db_obj)
            db.session.commit()
        except ValueError:
            return 500
        return 201

    def read_many(self, page):
        """read many method"""
        page_db_result = Movies.query.filter().paginate(page, 10, False).items
        if page_db_result:
            result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500

    def delete(self, movie_id: int):
        """delete movie method"""
        film = db.session.query(Movies).filter(Movies.movie_id == movie_id).first()
        if film:
            db.session.delete(film)
            db.session.commit()
            return 200
        return 500

    def read_filtered_by_name(self, page, genre: Dict):
        """get filtered by name results"""
        page_db_result = Movies.query.filter(
            Movies.genres.any(Genres.name == genre["name"])
        ).paginate(page, 10, False).items
        if page_db_result:
            result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500

    def read_filter_by_director(self, page, director: Dict):
        """get filtered by directors results"""
        page_db_result = Movies.query.filter(Movies.directors.any(
            Directors.name == director["name"]
        )).paginate(page, 10, False).items
        if page_db_result:
            result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500

    def read_filter_by_date_range(self, page, date_range: Dict):
        """get filtered by date range results"""
        page_db_result = Movies.query.filter(
            Movies.release_date.between(date_range["start"], date_range["end"]))\
            .paginate(page, 10, False).items
        if page_db_result:
            result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500

    def read_sort_by_rating(self, page):
        """get sorted by rating results"""
        page_db_result = Movies.query.order_by(Movies.rating).paginate(page, 10, False).items
        if page_db_result:
            result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500

    def read_sort_by_date(self, page):
        """get sorted by date results"""
        page_db_result = Movies.query.order_by(Movies.release_date).paginate(page, 10, False).items
        if page_db_result:
            result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500

    def update(self, data: MoviesSchema, movie_id: Optional[int]):
        """update method"""
        movie = Movies.query.filter_by(movie_id=movie_id).first()
        if movie:
            movie.name = data["name"]
            movie.release_date = data["release_date"]
            movie.description = data["description"]
            movie.rating = data["rating"]
            movie.poster_url = data["poster_url"]
            movie.user_id = data["user_id"]
            db.session.commit()
            return 201
        return 500


movie_repo = MovieRepo()
