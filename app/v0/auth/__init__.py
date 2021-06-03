from flask import Blueprint
from app.v0.auth.views import LoginView, RegisterView

auth = Blueprint("auth", __name__)
login_view = LoginView.as_view('login_view')
register_view = RegisterView.as_view('register_view')

auth.add_url_rule("/v0/login", view_func=login_view)
auth.add_url_rule("/v0/login/<string:access_token>", view_func=login_view, methods=["GET"])
auth.add_url_rule("/v0/signup", view_func=register_view)