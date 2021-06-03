from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_caching import Cache

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from app.config import Config
import os

TIMEOUT = 1800

basedir = os.path.dirname(os.path.abspath(__file__))

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
cache = Cache()

 
def create_db():
    db.create_all()

def create_app(name):
    app = Flask(name)
    
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    cache.init_app(app)

    manager = Manager(app)
    manager.add_command("db", MigrateCommand)

    
    from app.v0 import (
        auth, 
        users,
        links
    )
    
    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(links)
    # app.register_blueprint(uploads)
    
    return app, manager

from app import models