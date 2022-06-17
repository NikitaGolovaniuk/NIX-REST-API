from flask import Flask
from app.cfg.config import BaseConfig
from flask_migrate import Migrate
from app.db import db

app = Flask(__name__)
app.config.from_object(BaseConfig)
db.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db, directory='./migration')

from app.schemas import directors
from app.schemas import user_groups
from app.schemas import users
from app.schemas import genres
from app.schemas import movies
