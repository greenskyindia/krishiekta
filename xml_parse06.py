#!/usr/local/bin/python3

#----XML Parser file for Business Line

import xml.etree.ElementTree as ET
from datetime import datetime
from xml_fetch02 import local_file

tree = ET.parse(local_file)
root = tree.getroot()

pdate = datetime.now()
pdate2 = pdate.strftime("%a, %d %b %Y %H:%M:%S ")

odate = datetime.strptime("Sat, 21 Aug 2013 02:02:15 ", "%a, %d %b %Y %H:%M:%S ")
odate2 = odate.strftime("%a, %d %b %Y %H:%M:%S ")


class DataBox:

	did = None	
	dtitle = ''
	dlink = ''
	ddate = ''
	dcounter = 0

	def __init__(self,val):
		self.did = val
		DataBox.dcounter = DataBox.dcounter + 1

D = []
ctr = 0

for child in root:
	print(child.tag, child.attrib, child.text)
	for sub_child in child:
#		print("\t",sub_child.tag, sub_child.attrib, sub_child.text)
		if sub_child.tag == 'item':
			D.append(DataBox(ctr))
			ctr = ctr+1
			D[-1].dtitle = sub_child[0].text
			D[-1].dlink = sub_child[2].text
			#chdate = datetime.strptime(sub_child[4].text, "%a, %d %b %Y %H:%M:%S +0530")
			#D[-1].ddate = chdate
			D[-1].ddate = sub_child[4].text

		
temp = root.findall("./channel/item/link")

for j in temp:
	print(j.text)

'''
try:
	print (D,"\n\n\n")
	for i in D:
		print("Title: ",i.dtitle)
		print("Link: ",i.dlink)
		print("Date: ",i.ddate)
		print("____________________________________________________________________________________________")
	
except:
	print("Error")
'''
