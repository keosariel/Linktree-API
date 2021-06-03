from flask import Blueprint
from app.v0.links.views import LinkView

links = Blueprint("links", __name__)
link_view = LinkView.as_view('link_view')

links.add_url_rule("/v0/links/<string:public_id>", view_func=link_view, methods=["GET", "DELETE", "PUT"])
links.add_url_rule("/v0/links", view_func=link_view, methods=["POST"])