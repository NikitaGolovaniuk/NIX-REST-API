"""User groups domen"""
# pylint: disable=R0913, R0903, E0401
from typing import Dict, Optional
from flaskr.crud.abstract_repo import AbstractRepository
from flaskr.schemas.user_groups import UserGroupsSchema


def add_user_group(data: Dict, repo: AbstractRepository):
    """add single user group"""
    schema = UserGroupsSchema(**data)
    return repo.create(user_group_schema=schema)


def get_user_groups(user_group_id: Optional[int], repo: AbstractRepository):
    """add single user group by id"""
    return repo.read(user_group_id)


def delete_user_groups(user_group_id: Optional[int], repo: AbstractRepository):
    """delete single user group by id"""
    return repo.delete(user_group_id)


def get_many_user_groups(page: Optional[int], repo: AbstractRepository):
    """add multiple user groups"""
    return repo.read_many(page)


def update_user_groups(data: Dict, user_group_id: Optional[int], repo: AbstractRepository):
    """update user group"""
    return repo.update(data, user_group_id)
