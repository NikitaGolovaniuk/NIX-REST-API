"""Movie domen"""
# pylint: disable=R0913, R0903, E0401
from typing import Dict, Optional
from flaskr.crud.abstract_repo import AbstractRepository
from flaskr.schemas.movies import MoviesSchema


def add_movie(data: Dict, repo: AbstractRepository):
    """method to add single movie"""
    db_obj = MoviesSchema(**data)
    return repo.create(movie_schema=db_obj)


def get_one_movie(movie_id: Optional[int], repo: AbstractRepository):
    """method to get single movie"""
    return repo.read(movie_id)


def get_many_movies(page: Optional[int], repo: AbstractRepository) -> Optional[AbstractRepository]:
    """method to get multiple movies"""
    return repo.read_many(page)


def delete_movie(movie_id: int, repo: AbstractRepository):
    """method to delete single movie by id"""
    return repo.delete(movie_id)


def update_movie(data: Dict, movie_id: Optional[int], repo: AbstractRepository):
    """method to update movie"""
    return repo.update(data, movie_id=movie_id)


def filter_by_genre(page: int, genre: Dict, repo: AbstractRepository):
    """get multiple movies filtered by genre"""
    return repo.read_filtered_by_name(page, genre)


def filter_by_director(page: int, director: Dict, repo: AbstractRepository):
    """get multiple movies filtered by director"""
    return repo.read_filter_by_director(page, director)


def filter_by_date_range(page: int, data_range: Dict, repo: AbstractRepository):
    """get multiple movies filtered by date range"""
    return repo.read_filter_by_date_range(page, data_range)


def sort_by_rating(page: int, repo: AbstractRepository):
    """get multiple movies sorted by rating"""
    return repo.read_sort_by_rating(page)


def sort_by_date(page: int, repo: AbstractRepository):
    """get multiple movie sorted by date"""
    return repo.read_sort_by_date(page)
