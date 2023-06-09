import app as app
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

static_dir = os.path.abspath('/app/static/')
project_root = os.path.dirname(__file__)

static_dir = os.path.join(project_root, '../static')


app = Flask(__name__, static_folder=static_dir)


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
