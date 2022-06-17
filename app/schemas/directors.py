from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from app.models.directors import Directors


class DirectorsSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Directors
        exclude = ['email']
        load_instance = True
        include_fk = True
        include_relationships = True

    director_id = auto_field()