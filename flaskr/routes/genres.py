"""routes for genres"""
# pylint: disable=R0913, R0903, E0401
from flask_restx import Resource, Namespace, fields
from flask import request
from flaskr.crud.genres_repo import genres_repo
from flaskr.domain.genres_domen import update_genre, add_genre, delete_genre, \
    get_many_genres, get_genre
from flaskr.utils.logfiles.genres import log_created_genre, log_deleted_genre, log_updated_genre

genres_api = Namespace(name="api/genres", description="api for genres")

genres_modl = genres_api.model('genres_modl', {
    'name': fields.String
})


@genres_api.route('/add', methods=['POST'])
class AddGenre(Resource):
    """add genre"""
    @genres_api.doc(body=genres_modl)
    def post(self):
        """post method"""
        input_data = request.json
        log_created_genre(input_data)
        return add_genre(data=input_data, repo=genres_repo)


@genres_api.route('/delete=<int:genre_id>', methods=['DELETE'])
class DeleteGenre(Resource):
    """delete genre"""
    @genres_api.doc()
    def delete(self, genre_id):
        """delete method"""
        log_deleted_genre(genre_id)
        return delete_genre(genre_id=genre_id, repo=genres_repo)


@genres_api.route('/get=<int:genre_id>', methods=['GET'])
class GetGenre(Resource):
    """get one genre by id"""
    @genres_api.doc()
    def get(self, genre_id):
        """get method"""
        return get_genre(genre_id=genre_id, repo=genres_repo)


@genres_api.route('/getall=<int:page>', methods=['GET'])
class GetManyGenres(Resource):
    """get many genres resource"""
    @genres_api.doc()
    def get(self, page):
        """get method"""
        return get_many_genres(page=page, repo=genres_repo)


@genres_api.route('/<int:genre_id>/update', methods=['POST'])
class UpdateGenres(Resource):
    """update genres resource"""
    @genres_api.doc(body=genres_modl)
    def post(self, genre_id):
        """post method"""
        input_data = request.json
        log_updated_genre(genre_id, input_data)
        return update_genre(data=input_data, genre_id=genre_id, repo=genres_repo)
