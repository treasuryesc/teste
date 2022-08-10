# Copyright (c) 2022, TEste and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Docteste(Document):
	parametros = frappe.get_doc('Param', 'DEFAULT')

