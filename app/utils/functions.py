from flask import jsonify, current_app, request
from app.errors import ERRORS_DESCRIPTION, ERRORS_STATUS_CODE
from app.status_codes import BAD_REQUEST, SUCCESS_NO_CONTENT

from app.models import User

from hashlib import md5
from time import localtime
import os

from app.models import Audience, View


MIME_TYPES = {
    "image/jpeg" : ".jpg",
    "image/gif"  : ".gif",
    "image/png"  : ".png"
}

def response_data(data, error_code=None, description="", error_data=None, status_code=200):
	data = data
	has_error   = True if error_code else False

	if not description:
		description = ERRORS_DESCRIPTION.get(error_code,"")

	if has_error and error_code:
		status_code = ERRORS_STATUS_CODE.get(error_code, BAD_REQUEST)

	ret_json = {
		"data" : data,
		"error_code"  : error_code,
		"has_error"   : has_error,
		"description" : description,
		"error_data"  : error_data,
		"status_code" : status_code
 	}

	return jsonify(ret_json), status_code


def get_current_audience(ip_addr):
	audience = (
		Audience.query.filter_by(unique_id=ip_addr)
		.first()
	)

	if not audience:
		audience = Audience(unique_id=ip_addr)
		audience.save()

		audience.set_public_id()
	return audience

def add_view(ip_addr, unique_id, state):
	audience = get_current_audience(ip_addr)

	if audience:
		viewed = (
			View.query.filter_by(
				audience_id=audience.id, 
				unique_id=unique_id, 
				state=state
			).first()
		)

	if not viewed:
		viewed = View(
			audience_id=audience.id, 
			unique_id=unique_id, 
			state=state
		)
		viewed.save()
		viewed.set_public_id()



def get_public_id(unique_id):
	return md5(str(unique_id).encode("UTF-8")).hexdigest()

def get_unique_filename():
	"""Generates a random string"""
	prefix = md5(str(localtime()).encode('utf-8')).hexdigest()
	return f"{prefix}_upload"


def save_media(image_data, mime_type, sub_dir=""):
	"""Save a file to the upload folder"""
	upload_folder = current_app.config.get("UPLOAD_FOLDER")
	if sub_dir:
		upload_folder = os.path.join(upload_folder, sub_dir)

	raw_data = image_data
    
	if mime_type in MIME_TYPES and raw_data:
		filename = get_unique_filename()
		ext = MIME_TYPES[mime_type]

		filename = f"{filename}{ext}" 

		file = os.path.join(upload_folder, filename)

		# TODO: Make it safe
		try:
			with open(file, "w") as fp:
				fp.write(raw_data)
			
			return filename, mime_type
		except Exception as err:
			pass

	return None, mime_type

def get_upload(filename, sub_dir=""):
	upload_folder = current_app.config.get("UPLOAD_FOLDER")
	if sub_dir:
		upload_folder = os.path.join(upload_folder, sub_dir)

	file = os.path.join(upload_folder, filename)

	if os.path.exists(file):
		with open(file, "r") as fp:
			raw_data = fp.read()

		return raw_data

	return None