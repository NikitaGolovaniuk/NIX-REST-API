from flask_restx import Resource, Namespace, fields
from app.crud.user_repo import user_repo
from app.domain.user_domen import add_user
from flask import request

user_api = Namespace(name="api/users", description="best api ever")

model = user_api.model('Model', {
    'name': fields.String,
    'username': fields.String,
    'password': fields.String,
})


@user_api.route('/post', methods=['POST'])
class AddUser(Resource):
    @user_api.doc(body=model)
    def post(self):
        input_data=request.json
        return add_user(data=input_data, repo=user_repo)
