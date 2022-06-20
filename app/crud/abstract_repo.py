from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def post(self, *args, **kwargs):
        pass

    @abstractmethod
    def get(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def get_many(self):
        pass





