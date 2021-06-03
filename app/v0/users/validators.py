from flask_jsonvalidator import (
    JSONValidator,
    StringValidator
)

from app.regex import USERNAME, PASSWORD, EMAIL

class UserValidator(JSONValidator):
    validators = {
        "name"        : StringValidator(nullable=True),
        "username"    : StringValidator(regex=USERNAME, nullable=False, err_msg="Invalid Username"),
        "email"       : StringValidator(regex=EMAIL, nullable=False, err_msg="Invalid Email address"),
        "description" : StringValidator(nullable=False, err_msg="Description field cannot be empty")
    }

class ChangePasswordValidator(JSONValidator):
    validators = {
        "old_password" : StringValidator(nullable=False),
        "new_password" : StringValidator(regex=PASSWORD, nullable=False, err_msg="Password must be at least 8 characters long and must contain at least one *capital letter [A-Z]* and one *number [0-9]*")
    }

class RequestPasswordChangeValidator(JSONValidator):
    validators = {
        "email"        : StringValidator(regex=EMAIL, nullable=False, err_msg="Invalid Email address")
    }
