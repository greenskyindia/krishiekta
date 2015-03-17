#!/usr/local/bin/python3

#--------------IMPORTS-------------#

#No imports



#------------CLASSES-------------#


#-----Class TagBox describes structure for the HTML Tree elements

class TagBox:

	tid = 0	
	tdepth = 0
	ttag_name = ''
	tattrib = None
	tdata = ''
	tparent = 0
	tchild = []
	tcounter = 0
	tcombined_name = ''

	def __init__(self,val):
		self.tid = val
		self.tchild = []
		TagBox.tcounter = TagBox.tcounter + 1

	def combined_name_creator(self) :
		self.tcombined_name = self.ttag_name
		for i in self.tattrib:
			if (i[0] == "id"):
				self.tcombined_name = self.tcombined_name + "#" + i[1]
			if (i[0] == "class"):
				self.tcombined_name = self.tcombined_name + "." + i[1]
			
