"""file with base repository"""
# pylint: disable=R0913, R0903, E0401
from flaskr.crud.abstract_repo import AbstractRepository


class BaseRepository(AbstractRepository):
    """BaseRepository class"""
    def create(self, *args, **kwargs):
        pass

    def read(self, *args, **kwargs):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def read_many(self):
        pass
