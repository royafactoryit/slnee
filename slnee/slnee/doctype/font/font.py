# Copyright (c) 2021, Weslati Baha Eddine and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Font(Document):
	def validate(self):
		if self.type =="Google Fonts" :
			self.css=self.googlelinks
	pass
