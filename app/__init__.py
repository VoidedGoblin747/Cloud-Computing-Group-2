from flask import Flask
from flask_pymongo import PyMongo

from config import Config

# templates live in app/templates, but our css/js are in the project-root /static
app = Flask(__name__, static_folder='../static', static_url_path='/static')
app.config.from_object(Config)

mongo = PyMongo(app)

# import the routes/models at the bottom so they can use "app" and "mongo"
from app import routes, models  # noqa: E402,F401
