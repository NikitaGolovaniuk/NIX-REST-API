"""file with Abstract repository"""
# pylint: disable=R0913, R0903, E0401
from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """Abstract repository class"""
    @abstractmethod
    def create(self, *args, **kwargs):
        """abstract create method"""

    @abstractmethod
    def read(self, *args, **kwargs):
        """abstract read method"""

    @abstractmethod
    def update(self):
        """abstract update method"""

    @abstractmethod
    def delete(self):
        """abstract delete method"""

    @abstractmethod
    def read_many(self):
        """abstract read_many method"""
