"""file with genres repository"""
# pylint: disable=R0913, R0903, E0401
from typing import Optional
from flaskr.crud.base_repo import BaseRepository
from flaskr.models.genres import Genres
from flaskr.schemas.genres import GenresSchema
from flaskr import db


class GenresRepo(BaseRepository):
    """genres repository class"""
    def read(self, genre_id: int):
        """read method"""
        db_obj = Genres.query.filter_by(genre_id=genre_id).first()
        if db_obj:
            user_data = GenresSchema.from_orm(db_obj).dict()
            return user_data
        return 500

    def create(self, genres_schema: GenresSchema):
        """create method"""
        db_obj = Genres(name=genres_schema.name)
        if db_obj:
            db.session.add(db_obj)
            db.session.commit()
            return 201
        return 500

    def update(self, data: GenresSchema, genre_id: Optional[int]):
        """update method"""
        genre = Genres.query.filter_by(genre_id=genre_id).first()
        if genre:
            genre.name = data["name"]
            db.session.commit()
            return 201
        return 500

    def delete(self, genre_id: int):
        """delete method"""
        genre = db.session.query(Genres).filter(Genres.genre_id == genre_id).first()
        if genre:
            db.session.delete(genre)
            db.session.commit()
            return 200
        return 500

    def read_many(self, page: int):
        page_db_result = Genres.query.filter().paginate(page, 10, False).items
        if page_db_result:
            result = [GenresSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500


genres_repo = GenresRepo()
