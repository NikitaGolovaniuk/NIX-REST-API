from flask_restx import Api
from app.routes.users import user_api
from app.routes.movies import movie_api

api = Api(
    title='Movie',
    version='1.0',
    description='best movie liv',
)

api.add_namespace(user_api)
api.add_namespace(movie_api)
