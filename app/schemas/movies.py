from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import fields
from app.models.movies import Movies
from app.schemas.users import UsersSchema


class MoviesSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Movies
        exclude = ['email']
        load_instance = True
        include_fk = True
        include_relationships = True

    movie_id = auto_field()
    user_id = fields.Nested(UsersSchema, many=True)

