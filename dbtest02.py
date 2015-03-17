#!/usr/local/bin/python3

#----IMPORTS----#

#--MySQL connector
import mysql.connector

#--Config for DB (ConnTST001)
from db_config02 import config


#---- MySQL INITIALIZATIONS----#

try:

	conn = mysql.connector.connect(**config)
	

except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))
        
cursor = conn.cursor ()


cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")



#------------CLASSES-------------#

class DBops:
	ctr = 0



	#-----------INSERT INTO

	def insert_into(self,table_name,fields,values):
		flen = len(fields)
		temp_field = ''
		temp_desc = ''
		for i in fields:
			if i != fields[-1]:
				temp_field = temp_field + i + ", "
			else:
				temp_field = temp_field + i

		j = 0
		while j< flen -1:
			temp_desc = temp_desc + "%s,"
			j = j+1

		temp_desc = temp_desc + "%s"

		full_str = "INSERT INTO " + table_name + " (" + temp_field + ") VALUES(" + temp_desc + ")"

		print (full_str)
		print ("-------------------")
		for i in values:
			print (i)

		try:
			conn.commit()
			cursor.execute(full_str, values)
			conn.commit()
			
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))



	'''
	def update_table(self,table_name,fields,where_condition):
		flen = len(fields)
		temp_field = ''
		for i in fields:
			if i != fields[-1]:
				temp_field = temp_field + i[0] + " = " + i[1] + ", "
			else:
				temp_field = temp_field + i[0] + " = " + i[1]

		full_str = "UPDATE " + table_name + " SET " + temp_field + " WHERE" + where_condition + ";"

		print (full_str)
		print ("-------------------")
		for i in values:
			print (i)

		cursor.execute(full_str)
		conn.commit()
	'''


#---- MySQL CLOSE----#

conn.commit()
cursor.close ()
conn.close ()




#============================================================================#





#---------OPERATIONS---------#

db_handler1 = DBops()

db_handler1.insert_into("table04", ["id", "name", "value", "remarks"], [7,"test7",42.2,"this is a test entry"])

#db_handler1.update_table("table04",{"name":"Rakshit Agrawal","value":9.3},'''id = 1''')


