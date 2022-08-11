# Copyright (c) 2022, TEste and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import inspect

class Docteste(Document):
	# Este método faz parte da classe Docteste
	@frappe.whitelist()
	def metodo_dentro(self):
		return "Metodo dentro da classe"

# Este método NÃO faz parte da classe Docteste
@frappe.whitelist()
def metodo_fora():
	return "Metodo fora da classe"	