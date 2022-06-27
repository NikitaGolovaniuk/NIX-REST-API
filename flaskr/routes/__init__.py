from flask_restx import Api
from flaskr.routes.users import user_api
from flaskr.routes.movies import movie_api
from flaskr.routes.user_groups import user_groups_api
from flaskr.routes.genres import genres_api
from flaskr.routes.directors import directors_api

api = Api(
    title='Movie library api',
    version='1.0',
    description='api for movie library',
)

api.add_namespace(user_api)
api.add_namespace(movie_api)
api.add_namespace(user_groups_api)
api.add_namespace(genres_api)
api.add_namespace(directors_api)