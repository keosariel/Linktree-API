from flask_jsonvalidator import (
    JSONValidator,
    StringValidator
)

class LinkValidator(JSONValidator):
    validators = {
        "title"  : StringValidator(nullable=False, err_msg="Title field cannot be empty"),
        "description" : StringValidator(nullable=True),
        "url"        : StringValidator(nullable=False, err_msg="URL field cannot be empty")
    }
    