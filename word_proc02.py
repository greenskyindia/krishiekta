#!/usr/local/bin/python3

import re
from collections import Counter

#text = "This is the first text piece to work on. He said What? Then they all exclaimed!! It contains the variables of text that will be used to split and calculate frequency. It should find out the element frequency.-Correspondent. My confusion(doubt) is regarding the word a** used by him!"


text = ''' 

Good demand spurted the prices of almost all varieties of tea at the Kochi tea auction. In Sale No. 43, the quantity on offer in dust CTC grade was 11,73,000 kg.

The market for select best and popular marks was steady to firm and sometimes dearer following quality.

Others were irregular and lower by Rs 5-10 and sometimes more. Though a better enquiry witnessed from upcountry buyers, there was less export demand.

Of the quantity of 6,000 kg on offer in orthodox dust, the market was fully firm to dearer. Exporters absorbed a small quantity.

In the best CTC dust, PD varieties quoted at Rs 97/115, RD grades fetched Rs 106/141, SRD ruled at Rs 115/150 and SFD stood at Rs 120/155.

Leaf sale

The leaf sale also witnessed a good demand and the quantity on offer in orthodox category was 120,500 kg. The market for Nilgiri Brokens whole leaf was dearer by Rs 5-10 and sometimes more.

Highgrown fannings sold around last level. Medium clean black well-made whole leaf and bolder brokens was fully firm to dearer.

Corresponding tippy grades was irregular and sometimes tended to ease and witnessed some withdrawals. Fannings from the same origin appreciated.

Good demand

Demand was good for CTC leaf and the quantity on offer was 67,000 kg. The market for good liquoring varieties barely remained steady. Others were irregular and lower by Rs 3-5 and noticed some withdrawals.

There has been a subdued demand from exporters, while Kerala and upcountry buyers absorbed small quantity offered.

In dust grade, Manjolai SFD quoted the best prices of Rs 163, followed by Manjolai SRD at Rs 158. In the leaf category, Chamraj FP-sup fetched the best prices of Rs 266 followed by Chamraj FOP-Sup (green tea) at Rs 261. '''



replacers = ['.','-','!','?','(',')','*',"""'""",'''"''']
common_words = ['a' , 'am' , 'an' , 'and' , 'are' , 'as' , 'at' , 'be' , 'Because' , 'been' , 'but' , 'by' , 'for' , 'from' , 'had' , 'has' , 'have' , 'he' , 'her' , 'his' , 'I' , 'if' , 'in' , 'is' , 'it' , 'its' , 'Like' , 'May' , 'Me' , 'mine' , 'of' , 'on' , 'Or' , 'shall' , 'she' , 'Should' , 'So' , 'that' , 'the' , 'their' , 'them' , 'Then' , 'there' , 'These' , 'they' , 'This' , 'Those' , 'to' , 'was' , 'were' , 'What' , 'When' , 'Where' , 'Which' , 'Who' , 'Whom' , 'will' , 'You' , 'Your']
#for i in common_words:
#	text = text.replace(i,'.')

words = re.findall(r'\w+', text.lower())

x = Counter(words).most_common()


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
