from app.links.routes import Links
from app import api

api.add_resource(Links, "/links/<string:public_id>","/links")
