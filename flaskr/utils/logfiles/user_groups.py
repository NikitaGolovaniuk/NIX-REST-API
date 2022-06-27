"""user_groups logging"""
# pylint: disable=R0913, R0903, E0401
from flaskr import app
from flaskr.schemas.user_groups import UserGroupsSchema


def log_created_user_group(user_groups: UserGroupsSchema):
    """logging when user group was created"""
    log_msg = "Added user group:\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, user_groups["name"])


def log_updated_user_group(user_groups: UserGroupsSchema):
    """logging when user group was updated"""
    log_msg = "Updated user group:\n"
    log_msg += "\tname: %s\n"

    app.logger.info(log_msg, user_groups["name"])


def log_deleted_user_group(user_group_id: int):
    """logging when user group was deleted"""
    log_msg = "Deleted user group\n"
    log_msg += "\tID: %s"

    app.logger.info(log_msg, user_group_id)
