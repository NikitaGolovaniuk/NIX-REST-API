from flask_restx import Resource, Namespace, fields
from app.crud.movie_repo import movie_repo
from flask import request, jsonify
from app.domain.movie_domen import add_movie

movie_api = Namespace(name="api/movie", description="my genius api")

MovieTestModel = movie_api.model('MovieTestModel', {
    'name': fields.String,
    'release_date': fields.DateTime(dt_format='rfc822'),
    'description': fields.String,
    'rating': fields.Integer,
    'poster_url': fields.Url,
    'directors': fields.String,
    'id_genre': fields.String,
    'user_id': fields.Integer,
})


@movie_api.route('/post', methods=['POST'])
class AddMovie(Resource):
    """Add movie -Will add registration later"""
    @movie_api.doc(body=MovieTestModel)
    def post(self):
        data = request.json
        return add_movie(data=data, repo=movie_repo)



