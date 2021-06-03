from flask import jsonify, request, current_app
from flask.views import MethodView

from app.models import Link
from app.utils.classes import JSONObject
from app.utils.functions  import response_data, add_view
from app.utils.decorators import login_required, args_check
from app.errors import E000, E010, E011, E012, E013
from app.v0.links.validators import LinkValidator


class LinkView(MethodView):

    def get(self, public_id):
        """Handles GET request"""
        
        with current_app.app_context():

            link = (
                Link.query.filter_by(public_id=public_id)
                .first()
            )

            if link:

                add_view(
                    ip_addr=request.remote_addr, 
                    unique_id=link.id, 
                    state="l"
                )

                res = (
                    response_data(
                        link.to_dict()
                    )
                )

                return res
            
        # E012 = Link Does Not Exist (404)
        res = response_data(
            data=None, 
            error_code=E012
        )

        return res

    @args_check(LinkValidator())
    @login_required()
    def post(self, current_user):
        """Handles POST request"""

        current_user_id = current_user["id"]

        json_data = JSONObject(request.json)

        with current_app.app_context():
            title = json_data.title.strip()
            description = json_data.description.strip()
            url         = json_data.url.strip()

            images = request.json.get("images", None)

            link = Link(
                title=title,
                description=description,
                url=url,
                user_id=current_user_id
            ) 

            link.save()

            # Setting Public ID
            link.set_public_id()

            res = (
                response_data(
                    link.to_dict()
                )
            )

            return res

        # E000 = Server Error
        res = response_data(
            data=None, 
            error_code=E000
        )

        return res

    @args_check(LinkValidator())
    @login_required()
    def put(self, current_user, public_id):
        """Handles PUT request"""

        current_user_id = current_user["id"]

        json_data = JSONObject(request.json)

        with current_app.app_context():
            title = json_data.title.strip()
            description = json_data.description.strip()
            url        = json_data.url.strip()
            images      = request.json.get("images", None)

            link = Link.query.filter_by(public_id=public_id).first()

            if link:
                if link.user_id == current_user_id:
                    link.title = title
                    link.description = description
                    link.url = url

                    link.save()
                    
                    res = (
                        response_data(
                            link.to_dict()
                        )
                    )

                    return res
                
                # E010 = User Cannot Edit Link
                res = response_data(
                    data=None, 
                    error_code=E010
                )

                return res

            # E012 = Link Does Not Exist (404)
            res = response_data(
                data=None, 
                error_code=E012
            )

            return res

        # E000 = Server Error
        res = response_data(
            data=None, 
            error_code=E000
        )

        return res

    @login_required()
    def delete(self, current_user, public_id):
        """Handles DELETE request"""

        current_user_id = current_user["id"]

        with current_app.app_context():
            link = Link.query.filter_by(public_id=public_id).first()

            if link:
                if link.user_id == current_user_id:
                    link.deleted = True
                    link.save()

                    res = response_data(
                        data=None
                    )

                    return res

                # E011 = User Cannot Delete Item
                res = response_data(
                    data=None, 
                    error_code=E011
                )

                return res

            # E012 = Link Does Not Exist (404)
            res = response_data(
                data=None, 
                error_code=E012
            )

            return res
        
        # E000 = Server Error
        res = response_data(
            data=None, 
            error_code=E000
        )

        return res

    


    


    