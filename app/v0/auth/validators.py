from flask_jsonvalidator import (
    JSONValidator,
    StringValidator
)

from app.regex import USERNAME, PASSWORD, EMAIL

class LoginValidator(JSONValidator):
    validators = {
        "email"    : StringValidator(nullable=False, err_msg="Invalid Email address"),
        "password" : StringValidator(nullable=False, err_msg="Password field cannot be empty")
    }
    
class RegisterValidator(JSONValidator):
    validators = {
        "username"  : StringValidator(regex=USERNAME,nullable=False, err_msg="Invalid Username"),
        "email"     : StringValidator(regex=EMAIL,nullable=False, err_msg="Invalid Email address"),
        "password"  : StringValidator(regex=PASSWORD,nullable=False, err_msg="Password must be at least 8 characters long and must contain at least one *capital letter [A-Z]* and one *number [0-9]*")
    }