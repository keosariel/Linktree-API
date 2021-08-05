from flask import (
	request,
	current_app
)
from flask_restful        import Resource
from app.utils.functions  import JSONResponse
from app.utils.decorators import args_check
from app.validators  import LoginValidator, SignupValidator
from app.models      import User

from app.error_codes import (
	E003, # Username Already Exists
	E004, # Email Already Exists
	E011, # Authentication Error
	E012, # SignUp Error
	E013, # Login Error
	E021  # User does not exists
)


class Login(Resource):

	@args_check(LoginValidator())
	def post(self, json_data):	
		"""Creates an **authorization token** for a user if successfully
		logged in

		JSON parameters:
			:param email: User's email
			:type  email: String
			:param password: User's password
			:type  password: String

		:return: JSON Object with a token value 

		Reference:
			/validators.py
		"""

		with current_app.app_context():
			email = json_data.email.strip().lower()
			password = json_data.password

			# Checks if User with `email` exists
			user = User.query.filter_by(email=email).first()

			if not user:
				return JSONResponse(code=E021)

			if not user.password_is_valid(password):

				# E013 = Login Error
				return JSONResponse(
					message="Incorrect username or password!", 
					code=E013
				)

			token = user.generate_token()

			return JSONResponse(data={ 'token' : token, "user": user.to_dict() })

		return JSONResponse(
			message="Error logging in this account",
			code=E014
		)

class SignUp(Resource):

	@args_check(SignupValidator())
	def post(self, json_data):
		"""Creates an **authorization token** for a user if successfully
		signed up

		JSON parameters:
			:param username: User's username
			:type  username: String
			:param email: User's email
			:type  email: String
			:param password: User's password
			:type  password: String

		:return: JSON Object with a token value 

		Reference:
			/validators.py
		"""
		
		with current_app.app_context():
			username = json_data.username.strip().lower()
			email    = json_data.email.strip().lower()
			password = json_data.password

			# Checks if User with `email` exists
			existing_user = User.query.filter_by(email=email).first()

			if existing_user:
				return JSONResponse(
					message="User with this email already exists!", 
					code=E004
				)

			# Checks if User with `username` exists
			existing_user = User.query.filter_by(username=username).first()

			if existing_user:
				return JSONResponse(
					message="User with this username already exists!", 
					code=E003
				)

			user = User(
				username = username,
				email    = email
			)

			# Hashing password
			user.set_password(password)
			user.save()

			# Setting public ID
			user.set_public_id()

			token = user.generate_token()

			return JSONResponse(data={ 'token' : token, "user": user.to_dict() })

		return JSONResponse(
			message="Error creating an account",
			code=E014
		)