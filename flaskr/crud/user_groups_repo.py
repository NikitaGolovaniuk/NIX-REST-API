"""file with user groups repository"""
# pylint: disable=R0913, R0903, E0401
from typing import Optional
from flaskr.crud.base_repo import BaseRepository
from flaskr.db import db
from flaskr.models.user_groups import UserGroups
from flaskr.schemas.user_groups import UserGroupsSchema


class UserGroupsRepo(BaseRepository):
    """user groups repo class"""
    def read(self, user_group_id: int):
        """read method"""
        page_db_result = UserGroups.query.filter_by(user_group_id=user_group_id).all()
        if page_db_result:
            result = [UserGroupsSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500

    def create(self, user_group_schema: UserGroups):
        """create method"""
        db_obj = UserGroups(name=user_group_schema.name)
        if db_obj:
            db.session.add(db_obj)
            db.session.commit()
            return 201
        return 500

    def update(self, data: UserGroups, user_group_id: Optional[int]):
        """update method"""
        user_group = UserGroups.query.filter_by(user_group_id=user_group_id).first()
        if user_group:
            user_group.name = data["name"]
            db.session.commit()
            return 201
        return 500

    def delete(self, user_group_id: int):
        """delete method"""
        user_group = db.session.query(UserGroups)\
            .filter(UserGroups.user_group_id == user_group_id).first()
        if user_group:
            db.session.delete(user_group)
            db.session.commit()
            return 200
        return 500

    def read_many(self, page):
        """read many method"""
        page_db_result = UserGroups.query.filter().paginate(page, 10, False).items
        if page_db_result:
            result = [UserGroupsSchema.from_orm(db_obj).dict() for db_obj in page_db_result]
            return result
        return 500


user_groups_repo = UserGroupsRepo()
