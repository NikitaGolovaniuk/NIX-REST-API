"""flask flaskr"""
from flask import Flask
from flask_migrate import Migrate
from flaskr.cfg.config import BaseConfig, TestConfig
app = Flask(__name__)
app.config.from_object(BaseConfig)
from flaskr.db import db
from flaskr.routes import auth
from flaskr.routes import api
from flaskr.utils.logging import log_config

db.init_app(app)
api.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db, directory='./migration')
log_config(app)






