#!/usr/local/bin/python3

#----IMPORTS----#

#--MySQL connector
import mysql.connector

#--URLLIB
import urllib.request

#--XML
import xml.etree.ElementTree as ET

#--DATETIME
from datetime import datetime

#--Config for DB
from db_config01 import config





#----INITIALIZATIONS----#

business_line = 'http://www.thehindubusinessline.com/industry-and-economy/agri-biz/?service=rss'
local_dest = 'data001/blgen004.xml'


#--FETCH FILE FROM URL

urllib.request.urlretrieve(business_line, local_dest)

file_to_parse = local_dest


#--Time format in Business Line File

bl_time_format = "%a, %d %b %Y %H:%M:%S +0530"

constraint_date = "Sat, 02 Sep 2013 21:02:15 +0530"


#--Class for XML data storage

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



#--XML Tree Tasks

tree = ET.parse(file_to_parse)
root = tree.getroot()

D = []
ctr = 0

src_name = "Business Line"

for child in root:
	print(child.tag, child.attrib, child.text)
	for sub_child in child:
		if sub_child.tag == 'item':
			D.append(DataBox(ctr))
			ctr = ctr+1
			D[-1].dtitle = sub_child[0].text
			D[-1].dlink = sub_child[2].text
			#chdate = datetime.strptime(sub_child[4].text, "%a, %d %b %Y %H:%M:%S +0530")
			#D[-1].ddate = chdate
			D[-1].ddate = sub_child[4].text
			temp1 = datetime.strptime(sub_child[4].text, bl_time_format)
			D[-1].dnumdate = temp1
			




print("__________________________Checking D________________")
for i in D:
		print("Title: ",i.dtitle)
		print("Link: ",i.dlink)
		print("Date: ",i.ddate)

print("_____________________________________________________________________")
# MySQL query to enter the data into our database

try:

	conn = mysql.connector.connect(**config)
	

except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))
        
cursor = conn.cursor ()


cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")

uidctr = 101

try:
	print (D,"Pushing data into the DB")
	for i in D:
		print("Title: ",i.dtitle)
		print("Link: ",i.dlink)
		print("Date: ",i.ddate)
		#cursor.execute ("INSERT INTO table02 (title, url,date,source)"
		#	"VALUES(%s, %s, %s, %s )",
		#	(i.dtitle,i.dlink,i.dnumdate,src_name))

		cursor.execute ("INSERT INTO raw_data (uid,source_id, url, date, date_string, title,content)"
			"VALUES(%s, %s, %s, %s, %s, %s, %s)",
			(uidctr, "1", i.dlink, i.dnumdate, i.ddate, i.dtitle,"temp"))

		uidctr = uidctr + 1

		conn.commit()
	
except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))




conn.commit()
cursor.close ()
conn.close ()



