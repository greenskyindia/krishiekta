from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Encountered a start tag:", tag)
		for i in attrs:
			print("\tAttribute:",i[0])
			print("\tValue:",i[1])
	def handle_endtag(self, tag):
		print("Encountered an end tag :", tag)
	def handle_data(self, data):
		print("Encountered some data  :", data)
	def getpos(self):
		print (self);


parser = MyHTMLParser(strict=False)


#	For reading from file directly

f= open('data001/blgen002.xml','r')

parser.feed(f.read())
 
