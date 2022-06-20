from app.crud.abstract_repo import AbstractRepository


class BaseRepository(AbstractRepository):
    def post(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get_many(self):
        pass


SuperRepo = BaseRepository()
