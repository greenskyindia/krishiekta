#!/usr/local/bin/python3

#--------------IMPORTS-------------#

from parsing_engine01 import ParsingEngine
from identifier_test02 import tlist


#------------CLASSES-------------#



#----------SEARCH FUNCTIONS--------#



class SearchRules:

	FinalData = ''
	SourceTagList = tlist

	Identifiers = ['title','content','keywords','location','image']

	ListLength = len(SourceTagList)


	def search_bl(self,Tree):
		num = 0
		i = 0
		temp = Tree[i]

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


