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
		self.tchild = []
		TagBox.tcounter = TagBox.tcounter + 1


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
			print ("Link or Meta Found")
		
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
		
		if (PEMain.T[-1].ttag_name in PEMain.ignore):
			print ("Link or Meta Found")
		
		else:
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
			print ("Data : ",i.tdata)
			print ("***Parent : ", i.tparent)
			print ("\tKids : ",i.tchild)
			print ("________________________________________________________________________")
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


