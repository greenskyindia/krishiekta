
#--Class for identifier list storage

class IdentifierBox:

	counter = 0
	indx = None

	identifier_id = 0
	identifier_type = ''
	page_type = ''
	source_name = ''
	value_condition = 0
	parsing_type = ''
	source_tag_list = []
	attribute = ''
	delimiter = ''
	recognizer_text = ''
	flow_file = ''
	options = ''
	error_check = ''


	def __init__(self):
		#self.indx = val
		self.source_tag_list = []
		#self.spec_tag_list = []
		IdentifierBox.counter = IdentifierBox.counter + 1

