"""file with directors repository"""
# pylint: disable=R0913, R0903, E0401
from typing import Optional
from flaskr.crud.base_repo import BaseRepository
from flaskr import db
from flaskr.schemas.directors import DirectorsSchema
from flaskr.models.directors import Directors


class DirectorsRepo(BaseRepository):
    """directors repository class"""
    def read(self, director_id: int):
        """read method"""
        db_obj = Directors.query.filter_by(director_id=director_id).first()
        user_data = DirectorsSchema.from_orm(db_obj).dict()
        return user_data

    def create(self, directors_schema: DirectorsSchema):
        """create method"""
        db_obj = Directors(name=directors_schema.name)
        if db_obj:
            db.session.add(db_obj)
            db.session.commit()
            return 201
        return 500

    def update(self, data: DirectorsSchema, director_id: Optional[int]):
        """update method"""
        director = Directors.query.filter_by(director_id=director_id).first()
        if director:
            director.name = data["name"]
            db.session.commit()
            return 201
        return 500

    def delete(self, director_id: int):
        """delete method"""
        director = db.session.query(Directors).filter(Directors.director_id == director_id).first()
        if director:
            db.session.delete(director)
            db.session.commit()
            return 200
        return 500

    def read_many(self, page: int):
        """read many method"""
        page_db_result = Directors.query.filter().paginate(page, 10, False).items
        result = [DirectorsSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
        if result:
            return 200
        return 500


directors_repo = DirectorsRepo()
