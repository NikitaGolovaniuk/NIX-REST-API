from app.crud.base_repo import BaseRepository
from typing import Dict
from app.db import db
from app.schemas.movies import MoviesSchema
from app.models.movies import Movies
from app.models.genres import Genres
from app.models.directors import Directors


class MovieRepo(BaseRepository):

    def read(self, movie_id):
        page_db_result = Movies.query.filter_by(movie_id=movie_id).all()
        result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
        return result


    def create(self, movie_schema: MoviesSchema):
        db_obj = Movies(name=movie_schema.name,
                        rating=movie_schema.rating,
                        release_date=movie_schema.release_date,
                        description=movie_schema.description,
                        poster_url=movie_schema.poster_url,
                        user_id=movie_schema.user_id,
                        )
        db.session.add(db_obj)
        db.session.commit()
        return MoviesSchema.from_orm(db_obj).dict()


    def read_many(self, page):
        page_db_result = Movies.query.filter().paginate(page, 10, False).items
        result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
        return result

    def delete(self, movie_id: int):
        film = db.session.query(Movies).filter(Movies.movie_id == movie_id).first()
        db.session.delete(film)
        db.session.commit()
        return 200


    def read_filtered_by_name(self, page, genre: Dict):
        page_db_result = Movies.query.filter(Movies.genres.any(Genres.name == genre["name"])).paginate(page, 10,
                                                                                                       False).items
        result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
        return result


    def read_filter_by_director(self, page, director: Dict):
        page_db_result = Movies.query.filter(Movies.directors.any(Directors.name == director["name"])).paginate(page, 10,
                                                                                                       False).items
        result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
        return result


    def read_filter_by_date_range(self, page, date_range: Dict):
        page_db_result = Movies.query.filter(Movies.release_date.between(date_range["start"], date_range["end"])).paginate(page, 10,
                                                                                                               False).items
        result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
        return result


    def read_sort_by_rating(self, page):
        page_db_result = Movies.query.order_by(Movies.rating).paginate(page, 10, False).items
        result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
        return result


    def read_sort_by_date(self, page):
        page_db_result = Movies.query.order_by(Movies.release_date).paginate(page, 10, False).items
        result = [MoviesSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
        return result


movie_repo = MovieRepo()
