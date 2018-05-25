import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
#bootstrap = Bootstrap()

def create_app(config_class = Config):
    app = Flask(__name__, template_folder='/Users/ppdfour/myblog2.0/app/templates',static_folder='/Users/ppdfour/myblog2.0/static')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    #bootstrap.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint,url_prefix='/api')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return app


from app import models
