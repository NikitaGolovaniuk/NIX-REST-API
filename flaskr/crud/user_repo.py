"""file with repo of users"""
# pylint: disable=R0913, R0903, E0401
from typing import Optional
from flaskr.crud.base_repo import BaseRepository
from flaskr.schemas.users import UsersSchema
from flaskr.db import db
from flaskr.models.users import Users

class UserRepo(BaseRepository):
    """user repo class"""
    def read(self, user_id: int):
        """read method"""
        db_obj = Users.query.filter_by(user_id=user_id).first()
        if db_obj:
            user_data = UsersSchema.from_orm(db_obj).dict()
            return user_data
        return 500

    def create(self, user_schema: UsersSchema):
        """create method"""
        try:
            db_obj = Users(name=user_schema.name,
                           username=user_schema.username,
                           password=user_schema.password,
                           user_group_id=user_schema.user_group_id)
            db.session.add(db_obj)
            db.session.commit()
            return 201
        except ValueError:
            return 500

    def update(self, data: UsersSchema, user_id: Optional[int]):
        """update method"""
        user = Users.query.filter_by(user_id=user_id).first()
        if user:
            user.name = data["name"]
            user.username = data["username"]
            user.password = data["password"]
            user.group_id = data["user_group_id"]
            db.session.commit()
            return 201
        return 500

    def delete(self, user_id: int):
        """delete method"""
        user = db.session.query(Users).filter(Users.user_id == user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return 200
        return 500

    def read_many(self, page: int):
        """read many method"""
        page_db_result = Users.query.filter().paginate(page, 10, False).items
        if page_db_result:
            result = [UsersSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500


user_repo = UserRepo()
