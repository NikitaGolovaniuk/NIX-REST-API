"""routes for directors"""
# pylint: disable=R0913, R0903, E0401
from flask_restx import Resource, Namespace, fields
from flask import request
from flaskr.crud.directors_repo import directors_repo
from flaskr.domain.directors_domen import add_director, delete_director, get_director,\
    get_many_directors, update_director
from flaskr.utils.logfiles.directors import log_created_director, log_deleted_director,\
    log_updated_director

directors_api = Namespace(name="api/directors", description="api for directors")

director_model = directors_api.model('director_model', {
    'name': fields.String,
})


@directors_api.route('/add', methods=['POST'])
class AddDirector(Resource):
    """add director"""
    @directors_api.doc(body=director_model)
    def post(self):
        """post method"""
        input_data = request.json
        log_created_director(input_data)
        return add_director(data=input_data, repo=directors_repo)


@directors_api.route('/delete=<int:director_id>', methods=['DELETE'])
class DeleteDirector(Resource):
    """delete director"""
    @directors_api.doc()
    def delete(self, director_id):
        """delete method"""
        log_deleted_director(director_id)
        return delete_director(director_id=director_id, repo=directors_repo)


@directors_api.route('/get=<int:director_id>', methods=['GET'])
class GetDirector(Resource):
    """get one director by id"""
    @directors_api.doc()
    def get(self, director_id):
        """get method"""
        return get_director(director_id=director_id, repo=directors_repo)


@directors_api.route('/getall=<int:page>', methods=['GET'])
class GetManyDirectors(Resource):
    """get many directors"""
    @directors_api.doc()
    def get(self, page):
        """get method"""
        return get_many_directors(page=page, repo=directors_repo)


@directors_api.route('/<int:director_id>/update', methods=['POST'])
class UpdateDirectors(Resource):
    """update directors"""
    @directors_api.doc(body=director_model)
    def post(self, director_id):
        """post method"""
        input_data = request.json
        log_updated_director(input_data, director_id)
        return update_director(data=input_data, director_id=director_id, repo=directors_repo)
