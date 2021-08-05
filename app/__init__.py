from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt  import Bcrypt
from app.config    import Config

from flask_script  import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(Config)     # adding Config

db  = SQLAlchemy(app)
api = Api(app)
bcrypt  = Bcrypt(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)



from app.auth  import *
from app.users import *
from app.links import *

from app.models import *


