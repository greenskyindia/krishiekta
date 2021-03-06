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

#parser.feed(f.read())



parser.feed('''<DIV class="arthead">TOPICS</DIV><A class="bold" href="http://www.thehindubusinessline.com/topics/?categoryId=52300">
agriculture <SPAN class="blpipe">|</SPAN></A> <A href="http://www.thehindubusinessline.com/topics/?categoryId=52307">
rice (commodity) <SPAN class="blpipe">|</SPAN></A> <A href="http://www.thehindubusinessline.com/topics/?categoryId=52308">
wheat (commodity) <SPAN class="blpipe">|</SPAN></A> <A class="bold" href="http://www.thehindubusinessline.com/topics/?categoryId=52644">
economy (general) <SPAN class="blpipe">|</SPAN></A> <A href="http://www.thehindubusinessline.com/topics/?categoryId=52655">
prices, inflation and deflation <SPAN class="blpipe">|</SPAN></A> </DIV></DIV> ''')
 
