"""Genres domen"""
# pylint: disable=R0913, R0903, E0401
from typing import Dict, Optional
from flaskr.crud.abstract_repo import AbstractRepository
from flaskr.schemas.genres import GenresSchema


def get_genre(genre_id: Optional[int], repo: AbstractRepository):
    """method to get single genre"""
    return repo.read(genre_id)


def add_genre(data: Dict, repo: AbstractRepository):
    """method to add genre"""
    schema = GenresSchema(**data)
    return repo.create(schema)


def delete_genre(genre_id: Optional[int], repo: AbstractRepository):
    """method to delete single genre by id"""
    return repo.delete(genre_id)


def get_many_genres(page: Optional[int], repo: AbstractRepository):
    """method to get multiple genres"""
    return repo.read_many(page)


def update_genre(data: Dict, genre_id: Optional[int], repo: AbstractRepository):
    """update genre"""
    return repo.update(data, genre_id)
