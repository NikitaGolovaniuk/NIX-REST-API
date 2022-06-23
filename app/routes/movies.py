from flask_restx import Resource, Namespace, fields
from app.crud.movie_repo import movie_repo
from flask import request, jsonify
from app.domain.movie_domen import add_movie, filter_by_genre, \
    filter_by_director, filter_by_date_range, sort_by_rating, \
    sort_by_date, get_one_movie, get_many_movies, delete_movie

movie_api = Namespace(name="api/movie", description="my genius api")


genre_model = movie_api.model('genre_model', {
    'name': fields.String
})

directors_model = movie_api.model('directors_model', {
    'name': fields.String
})

MovieTestModel = movie_api.model('MovieTestModel', {
    'name': fields.String(required=False),
    'release_date': fields.DateTime(dt_format='rfc822'),
    'description': fields.String,
    'rating': fields.Integer,
    'poster_url': fields.Url,
    'directors': fields.List(fields.Nested(model=directors_model)),
    'id_genre': fields.List(fields.Nested(model=genre_model)),
    'user_id': fields.Integer,
})

date_range = movie_api.model('date_range', {
    'start': fields.DateTime(dt_format='rfc822'),
    'end': fields.DateTime(dt_format='rfc822'),
})


@movie_api.route('/id=<int:id>', methods=['GET'])
class GetOneMovie(Resource):
    """Get one movie -Will add registration later"""
    @movie_api.doc()
    def get(self, id):
        result = get_one_movie(movie_id=id, repo=movie_repo)
        return jsonify(result)


@movie_api.route('/page=<int:page>', methods=['GET'])
class GetManyMovies(Resource):
    """Get all movies with pagination -Will add registration later"""
    @movie_api.doc()
    def get(self, page):
        result = get_many_movies(page=page, repo=movie_repo)
        return jsonify(result)


@movie_api.route('/addmovie', methods=['POST'])
class AddMovie(Resource):
    """Add movie -Will add registration later"""
    @movie_api.doc(body=MovieTestModel)
    def post(self):
        data = request.json
        return add_movie(data=data, repo=movie_repo)


@movie_api.route('/id=<int:id>', methods=['DELETE'])
class DelMovie(Resource):
    """Delete movie -Will add registration later"""
    @movie_api.doc()
    def delete(self, id):
        return delete_movie(movie_id=id, repo=movie_repo)


@movie_api.route('/filter/genre/page=<int:page>')
class FilterByGenre(Resource):
    """Filter by genre"""
    @movie_api.doc(body=genre_model)
    def post(self, page):
        result = filter_by_genre(page=page, genre=request.json, repo=movie_repo)
        return jsonify(result)


@movie_api.route('/filter/director/page=<int:page>')
class FilterByDirector(Resource):
    """Filter by directors"""
    @movie_api.doc(body=directors_model)
    def post(self, page):
        result = filter_by_director(page=page, genre=request.json, repo=movie_repo)
        return jsonify(result)


@movie_api.route('/filter/daterange/page=<int:page>')
class FilterByDateRange(Resource):
    """Filter by date range"""
    @movie_api.doc(body=date_range)
    def post(self, page):
        result = filter_by_date_range(page=page, data_range=request.json, repo=movie_repo)
        return jsonify(result)


@movie_api.route('/sort/rating/page=<int:page>')
class SortByRating(Resource):
    """Sort by rating"""
    @movie_api.doc()
    def post(self, page):
        result = sort_by_rating(page=page, repo=movie_repo)
        return jsonify(result)


@movie_api.route('/sort/releasedate/page=<int:page>')
class SortByReleaseDate(Resource):
    """Sort by release date"""
    @movie_api.doc()
    def post(self, page):
        result = sort_by_date(page=page, repo=movie_repo)
        return jsonify(result)




