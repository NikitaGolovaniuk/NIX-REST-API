"""Module with logging configuration"""
# pylint: disable=R0913, R0903, E0401
import os
import logging


def log_config(app):
    """logger config"""
    dir_name = "logs/api.log"
    os.makedirs(os.path.dirname(dir_name), exist_ok=True)
    handler = logging.FileHandler("logs/api.log")
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
