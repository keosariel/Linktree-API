from flask_jsonvalidator import (
    JSONValidator,
    StringValidator,
    IntValidator,
    BooleanValidator,
    ArrayOfValidator
)

USERNAME = "^[a-z0-9_]{3,15}$"
EMAIL    = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
PASSWORD = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"

class LoginValidator(JSONValidator):
    validators = {
        "email"  : StringValidator(nullable=False),
        "password" : StringValidator(nullable=False),
    }

class SignupValidator(JSONValidator):
    validators = {
        "username"  : StringValidator(regex=USERNAME, nullable=False),
        "email"  : StringValidator(regex=EMAIL, nullable=False),
        "password" : StringValidator(nullable=False)
    }

class LinkValidator(JSONValidator):
    validators = {
        "title"  : StringValidator(nullable=False, err_msg="Title field cannot be empty"),
        "description" : StringValidator(nullable=True),
        "url"        : StringValidator(nullable=False, err_msg="URL field cannot be empty")
    }
    
class UserValidator(JSONValidator):
    validators = {
        "name"        : StringValidator(nullable=True),
        "username"    : StringValidator(regex=USERNAME, nullable=True, err_msg="Invalid Username"),
        "email"       : StringValidator(regex=EMAIL, nullable=True, err_msg="Invalid Email address"),
        "description" : StringValidator(nullable=False, err_msg="Description field cannot be empty")
    }