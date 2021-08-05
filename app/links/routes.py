from flask import (
	request,
	current_app
)
from flask_restful import Resource
from app.utils.functions import JSONResponse
from app.utils.decorators import args_check, login_required
from app.models import Link
from app.validators import LinkValidator

from app.error_codes import (
	E031, # Link Does Not Exists
	E032, # Cannot Delete this Link
	E033, # Cannot Edit this Link
	E034, # Error Editing Link
	E035, # Error Deleting Link
	E036  # Error Adding Link
)

class Links(Resource):

	def get(self, public_id):
		"""Queries the database for an existing Link item
		with the `public_id`	

		:return: A Link's JSON Object representation
			See: app.models `Link.to_dict()`
		"""

		with current_app.app_context():

			link = (
				Link.query.filter_by(public_id=public_id)
				.first()
			)

			if link:
				return JSONResponse(data=link.to_dict())

		# E031 = Link Does Not Exist
		return JSONResponse(code=E031)

	@args_check(LinkValidator())
	@login_required()
	def post(self, current_user, json_data):
		"""Creating/Adding a new Link

		Note: Request must be made with as Authorized Bearer token

		JSON parameters:
			:param title: Link's title
			:type  title: String
			:param description: Link's description
			:type  description: String
			:param url: User's website (a valid URL)
			:type  url: String

		:return: A Link's JSON Object representation
			See: app.models `Link.to_dict()` 
		"""

		with current_app.app_context():
			title = json_data.title.strip()
			description = json_data.description.strip()
			url         = json_data.url.strip()

			link = Link(
				title=title,
				description=description,
				url=url,
				user_id=current_user.id
			) 

			link.save()

			# Setting Public ID
			link.set_public_id()

			return JSONResponse(data=link.to_dict())

		# E036 = Error Adding Link
		return JSONResponse(code=E036)

	@args_check(LinkValidator())
	@login_required()
	def put(self, public_id, json_data, current_user):
		"""Editing/Updating Link

		Note: Request must be made with as Authorized Bearer token

		JSON parameters:
			:param title: Link's title
			:type  title: String
			:param description: Link's description
			:type  description: String
			:param url: User's website (a valid URL)
			:type  url: String

		:return: A Link's JSON Object representation
			See: app.models `Link.to_dict()` 
		"""

		with current_app.app_context():
			title = json_data.title.strip()
			description = json_data.description.strip()
			url         = json_data.url.strip()

			link = Link.query.filter_by(public_id=public_id).first()

			if not link:

				# E031 = Link Does Not Exist
				return JSONResponse(code=E031)

			if link.user_id != current_user.id:

				# E033 = User Cannot Edit Link
				return JSONResponse(code=E033)

			link.title = title
			link.description = description
			link.url = url

			link.save()

			return JSONResponse(data=link.to_dict())     

		# E034 = Error Editing Link
		return JSONResponse(code=E034)

	@login_required()
	def delete(self, current_user, public_id):
		"""Deleting link with the `public_id`
		
		Note: Request must be made with as Authorized Bearer token
		
		:return: None
		"""

		with current_app.app_context():
			link = Link.query.filter_by(public_id=public_id).first()

			if not link:

				# E031 = Link Does Not Exist
				return JSONResponse(code=E031)

			if link.user_id != current_user.id:

				# E032 = User Cannot Delete Link
				return JSONResponse(code=E032)

			link.deleted = True
			link.save()

			return JSONResponse(data=link.to_dict()) 

		# E035 = Error Deleting Link
		return JSONResponse(code=E035)