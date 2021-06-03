from flask import request, current_app
from flask.views import MethodView

from app.utils.functions  import response_data
from app.utils.classes    import JSONObject
from app.utils.decorators import args_check
from app.v0.auth.validators import LoginValidator, RegisterValidator
from app.errors import E005, E006, E015, E016, E017
from app.models import User



class LoginView(MethodView):

    def get(self, access_token):
        try:
            if access_token:
                valid, user_id = User.decode_token(access_token.strip())
                if valid:
                    user = User.query.get(user_id)
                    if user:
                        res = (
                            response_data(
                                { "islogged_in" : True, "username" : user.username }
                            )
                        )
                        return res

        except Exception as err:
            print(err)
            
        res = (
            response_data(
                { "islogged_in" : False , "username" : None}
            )
        )

        return res


    @args_check(LoginValidator())
    def post(self):
        """Handles POST request"""

        json_data = JSONObject(request.json)

        with current_app.app_context():
            email = (
                json_data.email.strip()
            )

            user = (
                User.query.filter_by(email=email)
                .first()
            )

            if user:
                if user.password_is_valid(json_data.password):
                    access_token = user.generate_token()

                    res = (
                        response_data(
                            { "access_token" : access_token, "username" : user.username  }
                        )
                    )

                    return res
		
        # E006 = Login Error
        res = response_data(
            data=None, 
            error_code=E006
        )

        return res


class RegisterView(MethodView):

    @args_check(RegisterValidator())
    def post(self):
        """Handles POST request"""

        json_data = JSONObject(request.json)

        with current_app.app_context():
            username  = json_data.username.lower().strip()
            email = json_data.email.strip()

            _user = User.query.filter_by(username=username).first()
            if _user:
                # E015 = Username Already Exists
                res = response_data(
                    data=None, 
                    error_code=E015
                )

                return res

            _user = User.query.filter_by(email=email).first()
            if _user:
                # E016 = Email Already Exists
                res = response_data(
                    data=None, 
                    error_code=E016
                )

                return res

            # Creating a User instance
            user = User(
                username = username,
                email    = email,
                password = json_data.password
            )

            # Adding instance to the database
            user.save()

            # Setting public id
            user.set_public_id()

            access_token = user.generate_token()

            res = (
                response_data(
                    { "access_token" : access_token, "username" : user.username }
                )
            )
			

            return res

        # E005 = SignUp Error
        res = response_data(
            data=None, 
            error_code=E005
        )

        return res




 