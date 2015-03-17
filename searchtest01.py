#!/usr/local/bin/python3

#--------------IMPORTS-------------#

from html.parser import HTMLParser



#------------CLASSES-------------#

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
			

class PEMain(HTMLParser):
	
	ctr = 0
	depth = 0
	gstack = []
	T=[]
#For Economic times
	ignore = ['link','meta','img','input','hr','br']

#For Business Line - link only




	def handle_starttag(self, tag, attrs):

		if (tag in PEMain.ignore):
			PEMain.T.append(TagBox(PEMain.ctr))
			PEMain.ctr = PEMain.ctr + 1
			PEMain.gstack.append(PEMain.T[-1].tid)
			PEMain.T[-1].depth = PEMain.depth
			PEMain.depth = PEMain.depth + 1
			PEMain.T[-1].ttag_name = tag
			PEMain.T[-1].tattrib = attrs
			PEMain.T[-1].combined_name_creator()
	#		if len(PEMain.gstack) > 1 :
			#print (PEMain.gstack)

		#	print ("Stack at Start of ",PEMain.T[-1].ttag_name,"..|..",tag," : ", PEMain.gstack)

			try:
				PEMain.T[-1].tparent = PEMain.gstack[-2]
				#print ("Gstack -2 : ",PEMain.gstack[-2])			
				#a = PEMain.gstack[-2]
				#b = PEMain.ctr - 1
		#		PEMain.T[a].tchild.append(b)
	#			PEMain.T[PEMain.gstack[-2]].tchild.append(PEMain.ctr - 1)
			#	print ("**Children of ", PEMain.T[-1].ttag_name," : ",PEMain.T[-1].tchild)
				PEMain.T[PEMain.gstack[-2]].tchild.append(PEMain.T[-1].tid)
			#	print ("##Children of ", PEMain.T[-1].ttag_name," : ",PEMain.T[-1].tchild)
	
			except:
				print ("Error")


		#	print ("Stack at end of ",PEMain.T[PEMain.gstack[-1]].ttag_name,"..|..",tag," : ", PEMain.gstack)

			PEMain.gstack.pop()
			PEMain.depth = PEMain.depth - 1
			
		else:
			PEMain.T.append(TagBox(PEMain.ctr))
			PEMain.ctr = PEMain.ctr + 1
			PEMain.gstack.append(PEMain.T[-1].tid)
			PEMain.T[-1].depth = PEMain.depth
			PEMain.depth = PEMain.depth + 1
			PEMain.T[-1].ttag_name = tag
			PEMain.T[-1].tattrib = attrs
			PEMain.T[-1].combined_name_creator()
	#		if len(PEMain.gstack) > 1 :
			#print (PEMain.gstack)

		#	print ("Stack at Start of ",PEMain.T[-1].ttag_name,"..|..",tag," : ", PEMain.gstack)

			try:
				PEMain.T[-1].tparent = PEMain.gstack[-2]
				#print ("Gstack -2 : ",PEMain.gstack[-2])			
			#	a = PEMain.gstack[-2]
			#	b = PEMain.ctr - 1
			#	PEMain.T[a].tchild.append(b)
	#			PEMain.T[PEMain.gstack[-2]].tchild.append(PEMain.ctr - 1)
			#	print ("**Children of ", PEMain.T[-1].ttag_name," : ",PEMain.T[-1].tchild)
				PEMain.T[PEMain.gstack[-2]].tchild.append(PEMain.T[-1].tid)
			#	print ("##Children of ", PEMain.T[-1].ttag_name," : ",PEMain.T[-1].tchild)
	
			except:
				print ("Error")
	
	def handle_endtag(self, tag):

		if (tag in PEMain.ignore):
			no_problem = 1
			#print ("Link or Meta Found")
		
		else:
		#	print ("Stack at end of ",PEMain.T[PEMain.gstack[-1]].ttag_name,"..|..",tag," : ", PEMain.gstack)			
			PEMain.gstack.pop()
			PEMain.depth = PEMain.depth - 1


			'''
			#print("Encountered an end tag :", tag)
			PEMain.ctr = PEMain.ctr -1
			print("**Current Counter: ",PEMain.ctr)		
			'''
	def handle_data(self, data):
		
		try:
			if (PEMain.T[-1].ttag_name in PEMain.ignore):
				no_problem = 1
				#print ("Link or Meta Found")
				#PEMain.T[PEMain.gstack[-1]].tdata = PEMain.T[PEMain.gstack[-1]].tdata + data
		
			else:
				try:
					PEMain.T[PEMain.gstack[-1]].tdata = PEMain.T[PEMain.gstack[-1]].tdata + data
	
				except:
					print ("Error")
					
				'''
				print("Encountered some data  :", data)
				print("**Current Counter: ",PEMain.ctr)
				'''
		except:
			print("No problem")

	def printTree(self):
		for i in PEMain.T:
			print ("Tag : ",i.ttag_name," --- ID: ",i.tid)
			#print ("Data : ",i.tdata)
			print ("***Parent : ", i.tparent)
			print ("\tKids : ",i.tchild)
			#i.combined_name_creator()
			print ("Combined Name : ",i.tcombined_name) 
			print ("________________________________________________________________________")
			#print ("Data : ",i.tdata)



#----------SEARCH FUNCTIONS--------#

#K = ["html","body#homebg","div#container","div#content","div#left-column","h1.detail-title"]
K = ["html","body#homebg","div#container","div#content","div#left-column","div#article-block","div.article-text","p.body"]
#K = ["html","body#homebg","div#container","div#content","div#left-column","div#article-block","div.article-text","div#articleKeywords","p","a"]



listlen = len(K)

print ("\nList length: " + str(listlen))



def search_bl(Tree):
	num = 0
	i = 0
	temp = Tree[i]
	finaldata = ''
	try:	
		while (num <= listlen+1):
			if(K[num] == temp.tcombined_name):
				print("Success at Level " + str(num) + " for tag in list as " + K[num] + " and tag in tree as " + temp.tcombined_name)
				#temp = Tree[i]
				#num = num +1
				for j in temp.tchild:
					if(Tree[j].tcombined_name == K[num+1]):
						f = Tree[j].tid
						temp = Tree[f]
						#num = num+1
						print("Level " +str(num) + " | Tag in tree as " + temp.tcombined_name)
						if(num == listlen-2):
							finaldata = finaldata + ";" + temp.tdata
							print ("\n\nData : " + finaldata)
				num = num + 1


	except:
		#finaldata = finaldata + temp.tdata
		print ("\n\nExcept Data : " + finaldata)



#---------OPERATIONS---------#


parser = PEMain()

#parser.initialize()

#	For reading from file directly

f= open('data001/bl_article_test.html','r')

parser.feed(f.read())

print("****************************************************")
print (parser)

	
print (parser.ctr)
print (parser.depth)
print("****************************************************")
print("****************************************************")
print("****************************************************")
#parser.printTree()
search_bl(parser.T)
print("****************************************************")


