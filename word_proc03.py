#!/usr/local/bin/python3

import re
from collections import Counter
from search_rules01 import SearchRules
#text = "This is the first text piece to work on. He said What? Then they all exclaimed!! It contains the variables of text that will be used to split and calculate frequency. It should find out the element frequency.-Correspondent. My confusion(doubt) is regarding the word a** used by him!"


text = SearchRules.FinalData


replacers = ['.','-','!','?','(',')','*',"""'""",'''"''']
common_words = ['a' , 'am' , 'an' , 'and' , 'are' , 'as' , 'at' , 'be' , 'Because' , 'been' , 'but' , 'by' , 'for' , 'from' , 'had' , 'has' , 'have' , 'he' , 'her' , 'his' , 'I' , 'if' , 'in' , 'is' , 'it' , 'its' , 'Like' , 'May' , 'Me' , 'mine' , 'of' , 'on' , 'Or' , 'shall' , 'she' , 'Should' , 'So' , 'that' , 'the' , 'their' , 'them' , 'Then' , 'there' , 'These' , 'they' , 'This' , 'Those' , 'to' , 'was' , 'were' , 'What' , 'When' , 'Where' , 'Which' , 'Who' , 'Whom' , 'will' , 'You' , 'Your']
#for i in common_words:
#	text = text.replace(i,'.')

words = re.findall(r'\w+', text.lower())

x = Counter(words).most_common()



print("****************************************************")
print(text)
print("****************************************************")
ctr = 0
for i in x:
	#print("--", i[0], " --")
	#ctr = ctr+1
	#print("CTR: = ",ctr)
	#print(x)
	if(x[ctr][0] in common_words):
	#	print ("Check!!!")
		#	del i
	#	print (ctr)
		x.pop(ctr)
		ctr = ctr - 1
	ctr = ctr+1


print(x)

l = len(x)

f = l//(2.5)
f= int(f)

y = x[0:f]

print("-------------------------------\n\n")
print(y)