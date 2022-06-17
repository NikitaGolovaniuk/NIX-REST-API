from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import fields
from app.models.users import Users
from app.schemas.user_groups import UserGroupsSchema


class UsersSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Users
        exclude = ['email']
        load_instance = True
        include_fk = True
        include_relationships = True

    user_id = auto_field()
    user_group_id = fields.Nested(UserGroupsSchema, many=True)
