from app.users.routes import Users
from app import api

api.add_resource(Users, "/users/<string:username>","/users")
