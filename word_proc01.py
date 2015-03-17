#!/usr/local/bin/python3

import re

text = "This is the first text piece to work on. He said What? Then they all exclaimed!! It contains the variables of text that will be used to split and calculate frequency. It should find ouot the element frequency.-Correspondent. My confusion(doubt) is regarding the word a** used by him!"

bkp = text

replacers = ['.','-','!','?','(',')','*',"""'""",'''"''']

for i in replacers:
	text = text.replace(i,' ')
	print (text,"\n---------")

text = text.lower()
print(text)


x = text.split()



print(x)
print("-----------------------------")


for i in x:
	print (i,":",x.count(i))
