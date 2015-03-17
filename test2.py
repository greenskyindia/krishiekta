#!/usr/local/bin/python3

import datetime
import mysql.connector
import sys


config = {
	'user': 'krishiekta',
	'password': 'krishiekta@123',
	'host': '192.168.1.116',
	'port':	'3306',
	'database': 'ConnTST001',
	'raise_on_warnings': True,
	}

# mysql query to enter the data into our database
try:

	conn = mysql.connector.connect(**config)
	

except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))
        
cursor = conn.cursor ()


cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")

r = range(63,76)
txt = "Text entry for loop"
val = 3.14
for x in r:
	txt2 = txt + str(x)
	val2 = val*x
	cursor.execute ("INSERT INTO table01 (id,name,value)"
			"VALUES(%s, %s, %s)",
			(x,txt2,val2))

	conn.commit()


	


conn.commit()
cursor.close ()
conn.close ()



