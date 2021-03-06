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
	tcounter = None


	def printall(self,d,t,a):
		self.tdepth = d
		self.ttag_name= t
		self.tattrib = a
		print("Depth as submitted by function: ",self.tdepth)
		print("Tag Name as submitted: ",self.ttag_name)
		print("Attrib as submitted: ",self.tattrib)


class PEMain(HTMLParser):
	
	tb1 = TagBox()

	def showall(self,d,t,a):
		self.tb1.tdepth = d
		self.tb1.ttag_name= t
		self.tb1.tattrib = a
		print("Depth as submitted by function: ",self.tb1.tdepth)
		print("Tag Name as submitted: ",self.tb1.ttag_name)
		print("Attrib as submitted: ",self.tb1.tattrib)

#	def initialize(self):
#		ctr
	ctr = 0
	T=[]
	def handle_starttag(self, tag, attrs):
		print("Encountered a start tag:", tag)
		PEMain.ctr = PEMain.ctr+1
		PEMain.T.append(tag)
		print("**Current Counter: ",PEMain.ctr)		
		#self.tname = tag
		for i in attrs:
			print("\tAttribute:",i[0])
			print("\tValue:",i[1])
	def handle_endtag(self, tag):
		print("Encountered an end tag :", tag)
		PEMain.ctr = PEMain.ctr -1
		print("**Current Counter: ",PEMain.ctr)		
	def handle_data(self, data):
		print("Encountered some data  :", data)
		print("**Current Counter: ",PEMain.ctr)
	def getpos(self):
		print ("Position :",self);

	def printT(self):
		#for i in PEMain.T:
		print(PEMain.T)




parser = PEMain()

#parser.initialize()

#	For reading from file directly

f= open('data001/file3download.html','r')

parser.feed(f.read())

print("****************************************************")
print (parser)

	
print (parser.ctr)

t1 = TagBox()

t1.printall("testdata","headtag","idattribute")

p1 = PEMain()

p1.showall("data_again","tagofchoice","attribs")

print("****************************************************")
print("****************************************************")
print("****************************************************")
print("****************************************************")
p1.printT()
