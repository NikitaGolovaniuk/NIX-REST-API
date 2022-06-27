"""users logging"""
# pylint: disable=R0913, R0903, E0401
from flaskr import app
from flaskr.schemas.users import UsersSchema


def log_created_user(users: UsersSchema):
    """logging when user was created"""
    log_msg = "Added user:\n"
    log_msg += "\tUsername: %s\n"
    log_msg += "\tName: %s\n"

    app.logger.info(log_msg, users["username"], users["name"])


def log_updated_user(users: UsersSchema):
    """logging when user was updated"""
    log_msg = "Updated user:\n"
    log_msg += "\tUser id: %s\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, users["user_id"], users["name"])


def log_deleted_user(user_id: int):
    """logging when user was deleted"""
    log_msg = "Deleted user\n"
    log_msg += "\tID: %s"

    app.logger.info(log_msg, user_id)
