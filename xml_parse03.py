import xml.etree.ElementTree as ET
from datetime import datetime

tree = ET.parse('data001/blgen003.xml')
root = tree.getroot()

pdate = datetime.now()
pdate2 = pdate.strftime("%a, %d %b %Y %H:%M:%S ")

odate = datetime.strptime("Sat, 21 Aug 2013 02:02:15 ", "%a, %d %b %Y %H:%M:%S ")
#odate = "Sat, 21 Aug 2013 02:02:15 "
odate2 = odate.strftime("%a, %d %b %Y %H:%M:%S ")

for child in root:
	print(child.tag, child.attrib, child.text)
	for sub_child in child:
#		print("\t",sub_child.tag, sub_child.attrib, sub_child.text)
		if sub_child.tag == 'item':
			chdate = datetime.strptime(sub_child[4].text, "%a, %d %b %Y %H:%M:%S +0530")
			#chdate2 = chdate.strftime("%a, %d %b %Y %H:%M:%S ")
			chdate2 = chdate.strftime("%A, %d  in the month of %B and the year %Y at time = %H:%M:%S ")
			print ("\t*** Date from text: ",chdate2)
			
			if sub_child[4].text < odate2:			
				for sub_child2 in sub_child:
			#	if sub_child2.text == 'International':
					print("\t\t",sub_child2.tag, sub_child2.attrib, sub_child2.text)

					for sub_child3 in sub_child2:
						print("\t\t\t",sub_child3.tag, sub_child3.attrib, sub_child3.text)
