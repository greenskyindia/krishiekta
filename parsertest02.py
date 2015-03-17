from html.parser import HTMLParser

class GenPE(HTMLParser):
	
	global depth
	#tag_name
	#tag_attribs
	#tag_data
	#tag_parent
	#tag_kids =[]
	tag_stack = []


	def myinit(self, depth, tag_name = None, tag_attribs = None, tag_data = None, tag_parent = None):
		self.depth = depth
		self.tag_name = tag_name
		self.tag_attribs = tag_attribs
		self.tag_data = tag_data
		self.tag_parent = tag_parent
		#self.rawdata = ''
		#self.lasttag = '???'
		#self.interesting = interesting_normal
		#self.cdata_elem = None


	def handle_starttag(self, tag, attrs):
		if depth ==0:
			self.tag_name = tag
			self.tag_attribs = attrs
			tag_stack.append(tag)
			depth = depth + 1
			#self.handle_data()

	"""	print("Encountered a start tag:", tag)
		for i in attrs:
			print("\tAttribute:",i[0])
			print("\tValue:",i[1])
	"""
	def handle_endtag(self, tag):
		print("Encountered an end tag :", tag)
	def handle_data(self, data):
		print("Encountered some data  :", data)
	def getpos(self):
		print (self);


parser = GenPE()


#	For reading from file directly

f= open('data001/filedownload.html','r')

parser.feed(f.read())
 
