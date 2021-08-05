from flask import request
from functools import wraps
from app.models import User
from app.utils.functions import JSONResponse
from app.utils.classes import JSONObject

from app.error_codes import (
    E002, # Invalid Request JSON
    E011  # Authentication Error
)

def login_required(optional=False):
    """
    Checks and validates the Authorization Header `Bearer Token`    
    if token is valid it'd set the `current_user`

    :param optional: If is set to `True` there wouldn't be any errors
                    if the token is invalid or expired 
    :type optional: Boolean
    """

    def _login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            # E011 = Authentication Error
            res = JSONResponse(
                code=E011,
                message="Not authorized, You need to Login!"
            )

            token = None

            try:
                auth_header = request.headers.get('Authorization')
                token = auth_header.split(" ")[1]
            except Exception:
                if not optional:
                    return res

            if token:
                valid, user_id = User.decode_token(token.strip())
                if valid:
                    user = User.query.get(user_id)
                    # kwargs["current_user"] = user

                    return f(*args, **kwargs, current_user=user)

            if optional:
                return f(*args, **kwargs, current_user=None)

            # E011 = Authentication Error
            res = JSONResponse(
                code=E011,
                message="Session expired, You need to Login"
            )

            return res

        return decorated_function
    return _login_required

def args_check(validator):
    """
    Checks and validates the JSON data been sent with a requests

    if JSON is valid based of the validator given it'd add 
    the `json_data` as a `kwarg`, os it'd be avaliable for
    futher use.
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            json_data = request.json if request.json else {}
            no_err, error_data = validator.validate(json_data)

            if not no_err:
                # E002 = Invalid Request JSON
                res = JSONResponse(
                    data=error_data, 
                    code=E002,
                )

                return res

            return f(*args, **kwargs, json_data=JSONObject(json_data))
        return decorated_function
    return decorator