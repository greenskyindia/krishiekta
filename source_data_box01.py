
#--Class for XML data storage

class SourceDataBox:

	item_id = None	
	item_title = ''
	item_link = ''
	item_date = ''
	item_tag_list = dict(date=None,title=None,url=None)

	item_numdate = ''
	counter = 0

	def __init__(self,val):
		self.item_id = val
		SourceBox.counter = SourceBox.counter + 1

