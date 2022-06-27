"""User domen"""
# pylint: disable=R0913, R0903, E0401
from typing import Dict, Optional
from flaskr.crud.abstract_repo import AbstractRepository
from flaskr.schemas.users import UsersSchema


def add_user(data: Dict, repo: AbstractRepository):
    """add single user"""
    schema = UsersSchema(**data)
    return repo.create(user_schema=schema)


def get_user(user_id: Optional[int], repo: AbstractRepository):
    """get single user"""
    return repo.read(user_id)


def delete_user(user_id: Optional[int], repo: AbstractRepository):
    """delete single user by id"""
    return repo.delete(user_id)


def get_many_users(page: Optional[int], repo: AbstractRepository):
    """get multiple users"""
    return repo.read_many(page)


def update_user(data: Dict, user_id: Optional[int], repo: AbstractRepository):
    """update single user"""
    return repo.update(data, user_id)
