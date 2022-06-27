"""routes for user_groups"""
# pylint: disable=R0913, R0903, E0401
from flask_restx import Resource, Namespace, fields
from flask import request
from flaskr.crud.user_groups_repo import user_groups_repo
from flaskr.domain.user_groups_domen import add_user_group, get_user_groups,\
    get_many_user_groups, delete_user_groups, update_user_groups
from flaskr.utils.logfiles.user_groups import log_created_user_group, \
    log_deleted_user_group, log_updated_user_group

user_groups_api = Namespace(name="api/user_groups", description="api for user_groups")

user_groups_api_model = user_groups_api.model('user_groups_api_model', {
    'name': fields.String,
})


@user_groups_api.route('/add', methods=['POST'])
class AddUserGroup(Resource):
    """add user_group"""
    @user_groups_api.doc(body=user_groups_api_model)
    def post(self):
        """post method"""
        input_data = request.json
        log_created_user_group(input_data)
        return add_user_group(data=input_data, repo=user_groups_repo)


@user_groups_api.route('/delete=<int:user_group_id>', methods=['DELETE'])
class DeleteUserGroup(Resource):
    """delete user_group"""
    @user_groups_api.doc()
    def delete(self, user_group_id):
        """delete method"""
        log_deleted_user_group(user_group_id)
        return delete_user_groups(user_group_id=user_group_id, repo=user_groups_repo)


@user_groups_api.route('/get=<int:user_group_id>', methods=['GET'])
class GetUserGroup(Resource):
    """get one user_group by id"""
    @user_groups_api.doc()
    def get(self, user_group_id):
        """get method"""
        return get_user_groups(user_group_id=user_group_id, repo=user_groups_repo)


@user_groups_api.route('/getall=<int:page>', methods=['GET'])
class GetManyUserGroups(Resource):
    """get many user_groups"""
    @user_groups_api.doc()
    def get(self, page):
        """get method"""
        return get_many_user_groups(page=page, repo=user_groups_repo)


@user_groups_api.route('/data/<int:user_group_id>/update', methods=['POST'])
class UpdateUserGroup(Resource):
    """update user_group"""
    @user_groups_api.doc(body=user_groups_api_model)
    def post(self, user_group_id):
        """post method"""
        input_data = request.json
        log_updated_user_group(input_data)
        return update_user_groups(data=input_data,
                                  user_group_id=user_group_id,
                                  repo=user_groups_repo)
