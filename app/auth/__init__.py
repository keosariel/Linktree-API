from app.auth.routes import Login, SignUp
from app import api

api.add_resource(Login, "/auth/login")
api.add_resource(SignUp, "/auth/signup")
