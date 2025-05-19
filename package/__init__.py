from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os

from .config import Config

db = SQLAlchemy()

from package.models import user

app = Flask(__name__, static_folder='../dist/assets')
CORS(app)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    if not os.path.exists('db.sqlite'):
        db.create_all()

from package.api import api
app.register_blueprint(api)
import package.ws