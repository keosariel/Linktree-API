from flask import Blueprint

users = Blueprint("users", __name__)

from app.v0.users.views import UserView

user_view = UserView.as_view('user_view')

users.add_url_rule("/v0/users/<string:username>", view_func=user_view, methods=["GET"])
users.add_url_rule("/v0/users", view_func=user_view)