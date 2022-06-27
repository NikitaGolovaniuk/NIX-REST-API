"""routes for users"""
# pylint: disable=R0913, R0903, E0401
from flask_restx import Resource, Namespace, fields
from flask import request
from flaskr.crud.user_repo import user_repo
from flaskr.domain.user_domen import add_user, get_user, delete_user, update_user, get_many_users
from flaskr.utils.logfiles.users import log_created_user, log_deleted_user, log_updated_user

user_api = Namespace(name="api/users", description="user api")

model = user_api.model('Model', {
    'name': fields.String,
    'username': fields.String,
    'password': fields.String,
    'user_group_id': fields.Integer,
})

update_model = user_api.model('update_model', {
    'user_id': fields.Integer,
    'name': fields.String,
    'username': fields.String,
    'password': fields.String,
    'user_group_id': fields.Integer,
})


@user_api.route('/add', methods=['POST'])
class AddUser(Resource):
    """add one user to database"""
    @user_api.doc(body=model)
    def post(self):
        """post method"""
        input_data = request.json
        log_created_user(input_data)
        return add_user(data=input_data, repo=user_repo)


@user_api.route('/delete=<int:user_id>', methods=['DELETE'])
class DeleteUser(Resource):
    """delete user"""
    @user_api.doc()
    def delete(self, user_id):
        """delete method"""
        log_deleted_user(user_id)
        return delete_user(user_id=user_id, repo=user_repo)


@user_api.route('/get=<int:user_id>', methods=['GET'])
class GetUser(Resource):
    """get one user by id"""
    @user_api.doc()
    def get(self, user_id):
        """get method"""
        return get_user(user_id=user_id, repo=user_repo)


@user_api.route('/getall=<int:page>', methods=['GET'])
class GetManyUsers(Resource):
    """get many users"""
    @user_api.doc()
    def get(self, page):
        """get method"""
        return get_many_users(page=page, repo=user_repo)


@user_api.route('/data/<int:user_id>/update', methods=['POST'])
class UpdateUser(Resource):
    """update user"""
    @user_api.doc(body=update_model)
    def post(self, user_id):
        """post method"""
        input_data = request.json
        log_updated_user(input_data)
        return update_user(data=input_data, user_id=user_id, repo=user_repo)
