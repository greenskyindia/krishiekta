#!/usr/local/bin/python3

#--------------IMPORTS-------------#

from parsing_engine01 import ParsingEngine
from identifier_test04 import identifier_ops

#source_tag_list, val_condition


#------------CLASSES-------------#



#----------SEARCH FUNCTIONS--------#



class SearchRules:

	FinalData = ''
	
	get_identifier_info = identifier_ops()

	identifier_object = get_identifier_info.identifier_information()
	
	SourceTagList = identifier_object.source_tag_list

	Identifiers = ['title','content','keywords','location','image']

	ListLength = len(SourceTagList)


	def search_bl(self,Tree):
		num = 0
		i = 0
		temp = Tree[i]

#		if(val_condition

		try:	
			while (num <= SearchRules.ListLength+1):
				if(SearchRules.SourceTagList[num] == temp.tcombined_name):
					for j in temp.tchild:
						if(Tree[j].tcombined_name == SearchRules.SourceTagList[num+1]):
							f = Tree[j].tid
							temp = Tree[f]
							if(num == SearchRules.ListLength-2):
								SearchRules.FinalData = SearchRules.FinalData + " " + temp.tdata
					num = num + 1
	
	
		except:
			print ("\n\nData : " + SearchRules.FinalData)
	



	def search_02(self,Tree):
		num = 0
		i = 0
		temp = Tree[i]

#		if(val_condition

		try:	
			while (num <= SearchRules.ListLength+1):

				if(SearchRules.SourceTagList[num] == temp.tcombined_name):

					for j in temp.tchild:

						if(Tree[j].tcombined_name == SearchRules.SourceTagList[num+1]):

							f = Tree[j].tid
							temp = Tree[f]

							if(num == SearchRules.ListLength-2):
								SearchRules.FinalData = SearchRules.FinalData + " " + temp.tdata
					num = num + 1
	
	
		except:
			print ("\n\nData : " + SearchRules.FinalData)
	
	





	
#---------OPERATIONS---------#
	

parser = ParsingEngine()

searcher = SearchRules()

#parser.initialize()

#	For reading from file directly

f= open('data001/bl_article_test.html','r')

parser.feed(f.read())

searcher.search_bl(parser.PageTree)
print("****************************************************")


