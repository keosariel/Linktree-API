from functools import wraps
from flask import jsonify, request, session, abort

from app.utils.classes   import JSONObject
from app.utils.functions import response_data
from app.errors import E004, E002
from app.models import User

import json

def args_check(validator):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            json_data = request.json if request.json else {}
            no_err, msg = validator.validate(json_data)
            
            if not no_err:
                # E002 = Invalid Request JSON
                res = response_data(
                    data=None, 
                    error_code=E002,
                    error_data=msg
                )

                return res

            return f(*args, **kwargs)
        return decorated_function
    return decorator

def login_required(optional=False):
    def _login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            
            # E004 = Authentication Error (406)
            res = response_data(
                data=None, 
                error_code=E004, 
                description="No Authorization Header"
            )

            access_token = None

            try:
                auth_header = request.headers.get('Authorization')
                access_token = auth_header.split(" ")[1]
            except Exception:
                if not optional:
                    return res

            if access_token:
                valid, user_id = User.decode_token(access_token.strip())
                if valid:
                    kwargs["current_user"] = { "id" : user_id }
                    return f(*args, **kwargs)

            if optional:
                kwargs["current_user"] = { "id" : None }
                return f(*args, **kwargs)

            # E004 = Authentication Error (406)
            res = response_data(
                data=None, 
                error_code=E004, 
                description="You need to Login"
            )

            return res

        return decorated_function
    return _login_required

def get_http_exception_handler(app):
    """Overrides the default http exception handler to return JSON."""
    
    handle_http_exception = app.handle_http_exception
    @wraps(handle_http_exception)
    def ret_val(exception):
        code = exception.code
        description = exception.description

        res = response_data (
            data=None,
            description=description,
            status_code=code
        )

        return res

    return ret_val