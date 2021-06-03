from app.status_codes import *

E000 = "E000"
E001 = "E001"
E002 = "E002"
E003 = "E003"
E004 = "E004"
E005 = "E005"
E006 = "E006"
E007 = "E007"
E008 = "E008"
E009 = "E009"
E010 = "E010"
E011 = "E011"
E012 = "E012"
E013 = "E013"
E014 = "E014"
E015 = "E015"
E016 = "E016"
E017 = "E017"
E018 = "E018"
E019 = "E019"


ERRORS_DESCRIPTION = {
	"E000" : "Bad request",
	"E001" : "Insufficient Parameters",
	"E002" : "An error occured, Make sure all fields are input correctly.", # Invalid Request JSON
	"E004" : "Login or Signup", # Authentication Error
	"E005" : "SignUp Error",
	"E006" : "Email or Password is incorrent",
	"E007" : "User Cannot Edit Profile",
	"E008" : "User Cannot Delete Profile",
	"E009" : "User Does Not Exist",
	"E010" : "User Cannot Edit Link",
	"E011" : "User Cannot Delete Link",
	"E012" : "Link Does Not Exist",
	"E013" : "Exceeded Maximum Number Of Uploads",
	"E014" : "Image Not Found",
	"E015" : "Username Already Exists",
	"E016" : "Email Already Exists",
	"E017" : "Incorrect Password",
	"E018" : "Email Doesn't Exists",
	"E019" : "Expired Token (Request another one)"
}


ERRORS_STATUS_CODE = {
	"E000" : BAD_REQUEST,
	"E001" : BAD_REQUEST,
	"E002" : BAD_REQUEST,
	"E004" : UNAUTHORIZED,
	"E005" : BAD_REQUEST,
	"E006" : UNAUTHORIZED,
	"E007" : UNAUTHORIZED,
	"E008" : UNAUTHORIZED,
	"E009" : NOT_FOUND,
	"E010" : UNAUTHORIZED,
	"E011" : UNAUTHORIZED,
	"E012" : NOT_FOUND,
	"E013" : BAD_REQUEST,
	"E014" : NOT_FOUND,
	"E015" : BAD_REQUEST,
	"E016" : BAD_REQUEST,
	"E017" : UNAUTHORIZED,
	"E018" : UNAUTHORIZED,
	"E019" : BAD_REQUEST
}