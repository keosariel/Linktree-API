from flask import (
	request,
	current_app
)
from flask_restful        import Resource
from app.utils.functions  import JSONResponse
from app.utils.decorators import args_check, login_required
from app.models      import User, SocialLink
from app.validators  import UserValidator

from app.error_codes import (
	E003, # Username Already Exists"
	E004, # Email Already Exists"
	E021, # User does not exists
	E022, # Cannot delete this user
	E023, # Cannot edit this user
	E024, # Error editing user
	E025  # Error deleting user
)

class Users(Resource):
	
	@login_required(optional=True)
	def get(self, username, current_user):

		"""Queries the database for an existing user
		with the `username`	

		:return: A user's JSON Object representation
			See: app.models `User.to_dict()`
		"""

		with current_app.app_context():

			user = (
				User.query.filter_by(username=username)
				.first()
			)

			if user:
				return JSONResponse(data=user.to_dict(user=current_user))

		# E021 = User Does Not Exist
		return JSONResponse(code=E021)


	@args_check(UserValidator())
	@login_required()
	def put(self, current_user, json_data):
		"""Updating/Editing user with the `username`

		Note: Request must be made with as Authorized Bearer token

		JSON parameters:
			:param username: User's new/existing username
			:type  username: String
			:param email: User's email
			:type  email: String
			:param description: User's new/existing description
			:type  description: String
			:param website: User's website (a valid URL)
			:type  website: String
			:param location: User's location
			:param type: String
			:param social_links: A list of dictionary objects with keys ["platform_id", "url"]
								:key type: Int
						  		:key url: A valid URL (String)

			:type  social_links: List[Dict]

		:return: A user's JSON Object representation
			See: app.models `User.to_dict()` 
		"""

		with current_app.app_context():

			name        = json_data.name.lower().strip()
			description = json_data.description.strip()
			username    = json_data.username.lower().strip()
			email       = json_data.email.lower().strip()
			website     = request.json.get("website", "")
			location    = request.json.get("location", "")

			social_links = request.json.get("social_links", None)


			if username != current_user.username and username:
				user = User.query.filter_by(username=username).first()

				if user:
					# E003 = Username Already Exists
					return JSONResponse(code=E003)

				# Update Username
				current_user.username = username

			if email != current_user.email and email:
				user = User.query.filter_by(email=email).first()

				if user:
					# E004 = Email Already Exists
					return JSONResponse(code=E004)

				# Update Email
				current_user.email = email

			if name:
				current_user.name = name

			if description:
				current_user.description = description

			if website:
				current_user.website = website

			if location:
				current_user.location = location

			if social_links:
				if type(social_links) == list:
					for social_link in social_links:
						if "platform_id" in social_link and "url" in social_link:
							# TODO: Check platform is if its int

							social_link_data = SocialLink.query.filter_by(
								platform_id=social_link.get("platform_id"),
								user_id=current_user.id
							).first()

							if social_link_data:
								social_link_data.url = social_link.get("url")
								social_link_data.save()
							else:   
								social_link_data = SocialLink (
									platform_id=social_link.get("platform_id"),
									url=social_link.get("url"),
									user_id=current_user.id
								)
								social_link_data.save()
								social_link_data.set_public_id()

			current_user.save()

			return JSONResponse(data=current_user.to_dict())

		# E024 = Error editing user
		return JSONResponse(code=E024)

	@login_required()
	def delete(self, current_user):
		"""Deleting user with the `username`
		
		Note: Request must be made with as Authorized Bearer token
		
		:return: None
		"""

		with current_app.app_context():
			current_user.deleted = True
			current_user.save()

			return JSONResponse(data=current_user.to_dict())

		# E025 = Error deleting user
		return JSONResponse(code=E025)

 