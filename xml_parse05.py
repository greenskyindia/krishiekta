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

			'''
			chdate = datetime.strptime(sub_child[4].text, "%a, %d %b %Y %H:%M:%S +0530")
			#chdate2 = chdate.strftime("%a, %d %b %Y %H:%M:%S ")
			chdate2 = chdate.strftime("%A, %d  in the month of %B and the year %Y at time = %H:%M:%S ")
			print ("\t*** Date from text: ",chdate2)
			
			if sub_child[4].text > odate2:			
				for sub_child2 in sub_child:
			#	if sub_child2.text == 'International':
					print("\t\t",sub_child2.tag, sub_child2.attrib, sub_child2.text)

					for sub_child3 in sub_child2:
						print("\t\t\t",sub_child3.tag, sub_child3.attrib, sub_child3.text)
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
