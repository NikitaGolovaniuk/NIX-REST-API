from app.crud.base_repo import BaseRepository
from typing import Dict
from app.db import db
from app.schemas.movies import MoviesSchema
from app.models.movies import Movies


class MovieRepo(BaseRepository):

    def get(self, data):
        print(data)
        value = Movies.query.filter_by(movie_id=data).paginate(1,10,False).items
        aboba = [MoviesSchema.from_orm(db_obj).dict() for db_obj in value]
        return aboba

    def post(self, data: Dict):
        tmp_list = []
        tmp_list.append(data.directors)
        tmp_list.append(data.id_genre)
        db_obj = Movies(
            name=data.name,
            release_date=data.release_date,
            description=data.description,
            rating=data.rating,
            poster_url=data.poster_url,
            directors=list(tmp_list[0]),
            id_genre=list(tmp_list[1]),
            user_id=data.user_id
        )
        db.session.add(db_obj)
        db.session.commit()
        return data


movie_repo = MovieRepo()