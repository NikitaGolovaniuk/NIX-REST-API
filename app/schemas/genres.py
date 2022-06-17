from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from app.models.genres import Genres


class GenresSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Genres
        exclude = ['email']
        load_instance = True
        include_fk = True
        include_relationships = True

    genre_id = auto_field()