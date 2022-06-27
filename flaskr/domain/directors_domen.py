"""Directors domen"""
# pylint: disable=R0913, R0903, E0401
from typing import Dict, Optional
from flaskr.crud.abstract_repo import AbstractRepository
from flaskr.schemas.directors import DirectorsSchema


def get_director(director_id: Optional[int], repo: AbstractRepository):
    """method to get single director"""
    return repo.read(director_id)


def add_director(data: Dict, repo: AbstractRepository):
    """method to add director"""
    schema = DirectorsSchema(**data)
    return repo.create(schema)


def delete_director(director_id: Optional[int], repo: AbstractRepository):
    """method to delete single director by id"""
    return repo.delete(director_id)


def get_many_directors(page: Optional[int], repo: AbstractRepository):
    """method to get multiple directors"""
    return repo.read_many(page)


def update_director(data: Dict, director_id: Optional[int], repo: AbstractRepository):
    """method to update single director"""
    return repo.update(data, director_id)
