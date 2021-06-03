# from app.custom_encrypt import create_map
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    DEBUG =  True             # some Flask specific configs
    CACHE_TYPE = "SimpleCache" # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 300
    
    UPLOAD_FOLDER = os.path.join(basedir, "uploads")

    STANDARD_TIMEOUT = 1800
