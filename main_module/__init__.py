from flask import Flask
from main_module.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

main_app = Flask(__name__)
main_app.config.from_object(Config)
db = SQLAlchemy(main_app)
migration = Migrate(main_app, db)

from main_module import routes, models
