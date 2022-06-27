"""directors logging"""
# pylint: disable=R0913, R0903, E0401
from flaskr import app
from flaskr.schemas.directors import DirectorsSchema


def log_created_director(input_data: DirectorsSchema):
    """logging when director was created"""
    log_msg = "Created director:\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, input_data["name"])


def log_updated_director(input_data: DirectorsSchema, director_id: int):
    """logging when director was updated"""
    log_msg = "Updated director:\n"
    log_msg += "\tID: %s\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, director_id, input_data["name"])


def log_deleted_director(director_id: int):
    """logging when director was deleted"""
    log_msg = "Deleted director\n"
    log_msg += "\tID: %s"

    app.logger.info(log_msg, director_id)
