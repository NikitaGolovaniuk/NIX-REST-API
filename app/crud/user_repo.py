from app.crud.base_repo import BaseRepository
from typing import Dict
from app.schemas.users import UsersSchema
from app.schemas.user_groups import UserGroupsSchema
from app.db import db
from app.models.users import Users
from app.models.user_groups import UserGroups

class UserRepo(BaseRepository):

    def read(self, kek: Dict):
        pass

    def create(self, user_schema: UsersSchema):
        db_obj = Users(name=user_schema.name,
                       username=user_schema.username,
                       password=user_schema.password,
                       user_group_id=user_schema.user_group_id)
        db.session.add(db_obj)
        db.session.commit()
        return UsersSchema.from_orm(db_obj).dict()


user_repo = UserRepo()

