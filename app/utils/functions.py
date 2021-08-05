from hashlib import md5
from time import localtime
from app.error_codes import ERRORS_DESCRIPTION, ERRORS_STATUS_CODE

def JSONResponse(data=None, message=None, code=None, status=200):

	if (not message and code) and code in ERRORS_DESCRIPTION:
		message = ERRORS_DESCRIPTION.get(code,"")

	if code and code in ERRORS_STATUS_CODE:
		status = ERRORS_STATUS_CODE.get(code)

	if code or status not in [200, 201]:
		return {
			"code": code,
			"message": message,
			"status": status,
			"data":data
		}, status
	else:
		return data

def get_public_id(unique_id):
	return md5(str(unique_id).encode("UTF-8")).hexdigest()

