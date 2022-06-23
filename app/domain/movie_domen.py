from typing import Dict
from app.crud.abstract_repo import AbstractRepository
from app.schemas.movies import MoviesSchema, MoviesSchemaAdd


def add_movie(data: Dict, repo: AbstractRepository):
    db_obj = MoviesSchema(**data)
    return repo.create(movie_schema=db_obj)


def get_one_movie(movie_id: int, repo: AbstractRepository):
    return repo.read(movie_id)


def get_many_movies(page: int, repo: AbstractRepository):
    return repo.read_many(page)


def delete_movie(movie_id: int, repo: AbstractRepository):
    return repo.delete(movie_id)


def filter_by_genre(page: int, genre: Dict, repo: AbstractRepository):
    return repo.read_filtered_by_name(page, genre)


def filter_by_director(page: int, director: Dict, repo: AbstractRepository):
    return repo.read_filter_by_director(page, director)


def filter_by_date_range(page: int, data_range: Dict, repo: AbstractRepository):
    return repo.read_filter_by_date_range(page, data_range)


def sort_by_rating(page: int, repo: AbstractRepository):
    return repo.read_sort_by_rating(page)


def sort_by_date(page: int, repo: AbstractRepository):
    return repo.read_sort_by_date(page)

