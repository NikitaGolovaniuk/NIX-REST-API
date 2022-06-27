"""genres logging"""
# pylint: disable=R0913, R0903, E0401
from flaskr import app
from flaskr.schemas.genres import GenresSchema


def log_created_genre(genre: GenresSchema):
    """logging when genre was created"""
    log_msg = "Added genre:\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, genre["name"])


def log_updated_genre(genre_id: int, input_data: GenresSchema):
    """logging when genre was updated"""
    log_msg = "Updated genre:\n"
    log_msg += "\tID: %s\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, genre_id, input_data["name"])


def log_deleted_genre(genre_id: int):
    """logging when genre was deleted"""
    log_msg = "Deleted genre\n"
    log_msg += "\tID: %s"

    app.logger.info(log_msg, genre_id)
