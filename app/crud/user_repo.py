from app.crud.base_repo import BaseRepository
from typing import Dict
from app.schemas.users import UsersSchema
from app.db import db
from app.models.users import Users


class UserRepo(BaseRepository):

    def get(self, kek: Dict):
        pass

    def post(self, user_schema: UsersSchema):
        db_obj = Users(name=user_schema.name, username=user_schema.username, password=user_schema.password)
        db.session.add(db_obj)
        db.session.commit()
        return UsersSchema.from_orm(db_obj).dict()


user_repo = UserRepo()

