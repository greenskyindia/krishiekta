#!/usr/local/bin/python3

#--------------IMPORTS-------------#

from html.parser import HTMLParser



#------------CLASSES-------------#

class TagBox:

	tid = None	
	tdepth = None
	ttag_name = None
	tattrib = None
	tdata = None
	tparent = None
	tchild = []
	tcounter = 0

	def __init__(self,val):
		self.tid = val
		TagBox.tcounter = TagBox.tcounter + 1


class PEMain(HTMLParser):
	
	ctr = 0
	depth = 0
	gstack = []
	T=[]

	def handle_starttag(self, tag, attrs):
		PEMain.T.append(TagBox(PEMain.ctr))
		PEMain.ctr = PEMain.ctr + 1
		PEMain.gstack.append(PEMain.T[-1].tid)
		PEMain.T[-1].depth = PEMain.depth
		PEMain.depth = PEMain.depth + 1
		PEMain.T[-1].ttag_name = tag
		PEMain.T[-1].tattrib = attrs
		
#		if len(PEMain.gstack) > 1 :
		#print (PEMain.gstack)

		try:
			PEMain.T[-1].tparent = PEMain.gstack[-2]
			#print ("Gstack -2 : ",PEMain.gstack[-2])			
			a = PEMain.gstack[-2]
			b = PEMain.ctr - 1
			PEMain.T[a].tchild.append(b)
#			PEMain.T[PEMain.gstack[-2]].tchild.append(PEMain.ctr - 1)
#			PEMain.T[PEMain.gstack[-2]].tchild.append(PEMain.T[-1].tid)

		except:
			print ("Error")

	def handle_endtag(self, tag):
		PEMain.gstack.pop()
		PEMain.depth = PEMain.depth - 1

		print (PEMain.gstack)
		'''
		#print("Encountered an end tag :", tag)
		PEMain.ctr = PEMain.ctr -1
		print("**Current Counter: ",PEMain.ctr)		
		'''
	def handle_data(self, data):
		try:
			PEMain.T[-1].tdata = data

		except:
			print ("Error")
				
		'''
		print("Encountered some data  :", data)
		print("**Current Counter: ",PEMain.ctr)
		'''

	def printTree(self):
		for i in PEMain.T:
			print ("Tag : ",i.ttag_name," --- ID: ",i.tid)
			#print ("\tKids : ",i.tchild)
			#print ("Parent : ", i.tparent)
			#print ("Data : ",i.tdata)


#---------OPERATIONS---------#


parser = PEMain()

#parser.initialize()

#	For reading from file directly

f= open('data001/file4download.html','r')

parser.feed(f.read())

print("****************************************************")
print (parser)

	
print (parser.ctr)
print (parser.depth)
print("****************************************************")
print("****************************************************")
print("****************************************************")
parser.printTree()
print("****************************************************")


