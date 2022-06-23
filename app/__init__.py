from flask import Flask
from app.cfg.config import BaseConfig
from flask_migrate import Migrate
from app.db import db

from app.routes import api

app = Flask(__name__)
app.config.from_object(BaseConfig)
db.init_app(app)
api.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db, directory='./migration')





