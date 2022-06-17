from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from app.models.user_groups import UserGroups


class UserGroupsSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = UserGroups
        exclude = ['email']
        load_instance = True
        include_fk = True
        include_relationships = True

    user_group_id = auto_field()



