#!/usr/local/bin/python3

#import datetime
import mysql.connector
import sys


import xml.etree.ElementTree as ET
from datetime import datetime


config = {
	'user': 'krishiekta',
	'password': 'krishiekta@123',
	'host': '192.168.1.116',
	'port':	'3306',
	'database': 'ConnTST001',
	'raise_on_warnings': True,
	}


file_to_parse = 'data001/blgen003.xml'

time_format = "%a, %d %b %Y %H:%M:%S +0530"

base_date = "Sat, 21 Aug 2013 02:02:15 +0530"

#db_time_format = "%Y-

class DataBox:

	did = None	
	dtitle = ''
	dlink = ''
	ddate = ''
	dnumdate = ''
	dcounter = 0

	def __init__(self,val):
		self.did = val
		DataBox.dcounter = DataBox.dcounter + 1




tree = ET.parse(file_to_parse)
root = tree.getroot()

pdate = datetime.now()
pdate2 = pdate.strftime(time_format)

odate = datetime.strptime(base_date, time_format)
odate2 = odate.strftime(time_format)


D = []
ctr = 0

src_name = "Business Line"

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
			temp1 = datetime.strptime(sub_child[4].text, time_format)
			D[-1].dnumdate = temp1
			




# mysql query to enter the data into our database
try:

	conn = mysql.connector.connect(**config)
	

except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))
        
cursor = conn.cursor ()


cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")


try:
	print (D,"Pushing data into the DB")
	for i in D:
		print("Title: ",i.dtitle)
		print("Link: ",i.dlink)
		print("Date: ",i.ddate)
		cursor.execute ("INSERT INTO table02 (title, url,date,source)"
			"VALUES(%s, %s, %s, %s )",
			(i.dtitle,i.dlink,i.dnumdate,src_name))

	conn.commit()
	
except:
	print("Error")




conn.commit()
cursor.close ()
conn.close ()



