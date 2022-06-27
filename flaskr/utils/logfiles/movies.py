"""movies logging"""
# pylint: disable=R0913, R0903, E0401
from flaskr import app
from flaskr.schemas.movies import MoviesSchema


def log_created_movie(movie: MoviesSchema):
    """logging when movie was created"""
    log_msg = "Added movie:\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, movie["name"])


def log_updated_movie(movie_id: int, movie: MoviesSchema):
    """logging when movie was updated"""
    log_msg = "Updated movie:\n"
    log_msg += "\tID: %s\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, movie_id, movie["name"])


def log_deleted_movie(movie_id: int):
    """logging when movie was deleted"""
    log_msg = "Deleted movie\n"
    log_msg += "\tID: %s"

    app.logger.info(log_msg, movie_id)
