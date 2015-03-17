#!/usr/local/bin/python3

#--------------IMPORTS-------------#

from html.parser import HTMLParser
from tag_box01 import TagBox



#------------CLASSES-------------#


#-----Class ParsingEngine is the Main HTML parser class. All parsing operations are handled by this class

class ParsingEngine(HTMLParser):
	
	ctr = 0		#Sequence counter
	depth = 0	#Stack dpeth
	gstack = []	#Stack of tags
	PageTree=[]	#Tree variable for main HTML tree

	ignore_list = ['link','meta','img','input','hr','br']





	def handle_starttag(self, tag, attrs):

		ParsingEngine.PageTree.append(TagBox(ParsingEngine.ctr))
		ParsingEngine.ctr = ParsingEngine.ctr + 1
		ParsingEngine.gstack.append(ParsingEngine.PageTree[-1].tid)
		ParsingEngine.PageTree[-1].depth = ParsingEngine.depth
		ParsingEngine.depth = ParsingEngine.depth + 1
		ParsingEngine.PageTree[-1].ttag_name = tag
		ParsingEngine.PageTree[-1].tattrib = attrs
		ParsingEngine.PageTree[-1].combined_name_creator()

		try:
			ParsingEngine.PageTree[-1].tparent = ParsingEngine.gstack[-2]
			ParsingEngine.PageTree[ParsingEngine.gstack[-2]].tchild.append(ParsingEngine.PageTree[-1].tid)
	
		except:
			print ("Error")

		
		if (tag in ParsingEngine.ignore_list):

			ParsingEngine.gstack.pop()
			ParsingEngine.depth = ParsingEngine.depth - 1
		

	def handle_endtag(self, tag):

		if (tag not in ParsingEngine.ignore_list):
			ParsingEngine.gstack.pop()
			ParsingEngine.depth = ParsingEngine.depth - 1


	def handle_data(self, data):
		
		try:
			if (ParsingEngine.PageTree[-1].ttag_name not in ParsingEngine.ignore_list):
				try:
					ParsingEngine.PageTree[ParsingEngine.gstack[-1]].tdata = ParsingEngine.PageTree[ParsingEngine.gstack[-1]].tdata + data
	
				except:
					print ("Error")
					
			
		except:
			print("No problem")



	def printTree(self):
		for i in ParsingEngine.PageTree:
			print ("Tag : ",i.ttag_name," --- ID: ",i.tid)
			#print ("Data : ",i.tdata)
			print ("***Parent : ", i.tparent)
			print ("\tKids : ",i.tchild)
			#i.combined_name_creator()
			print ("Combined Name : ",i.tcombined_name) 
			for j in i.tattrib:
				print("Attrib name : ",j[0])
			print ("________________________________________________________________________")
			#print ("Data : ",i.tdata)

	
#---------OPERATIONS---------#
	
#No operations
