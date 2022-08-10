# Copyright (c) 2022, TEste and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Docteste(Document):
	try: 
		parametros = frappe.get_doc('Param', 'DEFAULT')
		break
	except DoesNotExistError:
		print("Oops!  That was no valid number.  Try again...")

