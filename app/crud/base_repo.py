from app.crud.abstract_repo import AbstractRepository


class BaseRepository(AbstractRepository):
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


SuperRepo = BaseRepository()
