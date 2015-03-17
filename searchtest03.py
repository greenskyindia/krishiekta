#!/usr/local/bin/python3

#--------------IMPORTS-------------#

from parsing_engine01 import ParsingEngine
from identifier_test02 import tlist


#------------CLASSES-------------#

			

#----------SEARCH FUNCTIONS--------#

#K = ["html","body#homebg","div#container","div#content","div#left-column","h1.detail-title"]
#K = ["html","body#homebg","div#container","div#content","div#left-column","div#article-block","div.article-text","p.body"]
#K = ["html","body#homebg","div#container","div#content","div#left-column","div#article-block","div.article-text","div#articleKeywords","p","a"]



class SearchRule:

	finaldata = ''
	K = tlist

	listlen = len(K)

	#print ("\nList length: " + str(listlen))



	def search_bl(self,Tree):
		num = 0
		i = 0
		temp = Tree[i]
		#Searchrule.finaldata = ''
		try:	
			while (num <= SearchRule.listlen+1):
				if(SearchRule.K[num] == temp.tcombined_name):
					#print("Success at Level " + str(num) + " for tag in list as " + SearchRule.K[num] + " and tag in tree as " + temp.tcombined_name)
					#temp = Tree[i]
					#num = num +1
					for j in temp.tchild:
						if(Tree[j].tcombined_name == SearchRule.K[num+1]):
							f = Tree[j].tid
							temp = Tree[f]
							#num = num+1
						#	print("Level " +str(num) + " | Tag in tree as " + temp.tcombined_name)
							if(num == SearchRule.listlen-2):
								SearchRule.finaldata = SearchRule.finaldata + " " + temp.tdata
								#print ("\n\nData : " + finaldata)
					num = num + 1
	
	
		except:
			#finaldata = finaldata + temp.tdata
			print ("\n\nData : " + SearchRule.finaldata)
	
	
	
#---------OPERATIONS---------#
	

parser = ParsingEngine()

searcher = SearchRule()

#parser.initialize()

#	For reading from file directly

f= open('data001/bl_article_test.html','r')

parser.feed(f.read())

searcher.search_bl(parser.PageTree)
print("****************************************************")


