# STATUS CODES
SUCCESS                = 200
SUCCESS_CREATED        = 201
SUCCESS_NO_CONTENT     = 204
NOT_MODIFIED           = 304
BAD_REQUEST            = 400
INVALID_PARAMETERS     = BAD_REQUEST
UNAUTHORIZED           = 401
NO_PERMISSION          = 401
FORBIDDEN              = 403
NOT_FOUND              = 404
CONFLICT               = 409
INTERNAL_SERVER_ERROR  = 500
FILE_TOO_LARGE         = 400 


# Validation Errors
E001 = "E001"
E002 = "E002"
E003 = "E003"
E004 = "E004"
E005 = "E005"
E006 = "E006"
E007 = "E007"
E008 = "E008"
E009 = "E009"

# Authentication
E011 = "E011"
E012 = "E012"
E013 = "E013"
E014 = "E014"
E015 = "E015"

# User Errors
E021 = "E021"
E022 = "E022"
E023 = "E023"
E024 = "E024"
E025 = "E025"

# Link Errors
E031 = "E031"
E032 = "E032"
E033 = "E033"
E034 = "E034"
E035 = "E035"
E036 = "E036"

# MISC
E041 = "E041"
E042 = "E042"
E043 = "E043"
E044 = "E044"
E045 = "E045"

ERRORS_DESCRIPTION = dict(
	E001 = "Insufficient Parameters",
	E002 = "Invalid Request JSON",
	E003 = "Username Already Exists",
	E004 = "Email Already Exists",
	E005 = "Exceeded Maximum Number Of Uploads",
	E006 = "E006",
	E007 = "E007",
	E008 = "E008",
	E009 = "E009",

	E011 = "Authentication Error",
	E012 = "SignUp Error",
	E013 = "Login Error",
	E014 = "Error Authenticating User",
	E015 = "E015",

	E021 = "User does not exists",
	E022 = "Cannot delete this user",
	E023 = "Cannot edit this user",
	E024 = "Error editing user",
	E025 = "Error deleting user",

	E031 = "Link does not exists",
	E032 = "User Cannot delete this link",
	E033 = "User Cannot edit this link",
	E034 = "Error editing link",
	E035 = "Error deleting link",
	E036 = "Error Adding Link",

	E041 = "Image Not Found",
	E042 = "E042",
	E043 = "E043",
	E044 = "E044",
	E045 = "E045",
)



ERRORS_STATUS_CODE = dict(
	E001 = BAD_REQUEST,
	E002 = BAD_REQUEST,
	E003 = BAD_REQUEST,
	E004 = BAD_REQUEST,
	E005 = BAD_REQUEST,
	E006 = "E006",
	E007 = "E007",
	E008 = "E008",
	E009 = "E009",

	E011 = BAD_REQUEST,
	E012 = BAD_REQUEST,
	E013 = BAD_REQUEST,
	E014 = BAD_REQUEST,
	E015 = BAD_REQUEST,

	E021 = NOT_FOUND,
	E022 = NO_PERMISSION,
	E023 = NO_PERMISSION,
	E024 = INTERNAL_SERVER_ERROR,
	E025 = INTERNAL_SERVER_ERROR,

	E031 = NOT_FOUND,
	E032 = NO_PERMISSION,
	E033 = NO_PERMISSION,
	E034 = BAD_REQUEST,
	E035 = BAD_REQUEST,
	E036 = BAD_REQUEST,

	E041 = NOT_FOUND,
	E042 = "E042",
	E043 = "E043",
	E044 = "E044",
	E045 = "E045",
)
