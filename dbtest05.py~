#!/usr/local/bin/python3

#----IMPORTS----#

#--MySQL connector
import mysql.connector

#--Config for DB (ConnTST001)
from db_config03 import config


#---- MySQL INITIALIZATIONS----#
'''
try:

	conn = mysql.connector.connect(**config)
	

except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))
        
cursor = conn.cursor ()


cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")
'''


#------------CLASSES-------------#

class DBops:

	ctr = 0


	def db_initiate(self):

		print("We're in the initiator!")
		try:
			self.conn = mysql.connector.connect(**config)
	
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))
        
		self.cursor = self.conn.cursor()

		self.cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")

		print("Bye Bye Initiator!")


	#-----------INSERT INTO

	def insert_into(self,table_name,fields,values):

		self.db_initiate()		


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

		full_str = "INSERT INTO " + config['database'] + '.' + table_name + " (" + temp_field + ") VALUES(" + temp_desc + ")"

		print (full_str)
		print ("-------------------")
		for i in values:
			print (i)

		try:
			#self.conn.commit()
			self.cursor.execute(full_str, values)
			self.conn.commit()
			
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))

		self.db_close()



	
	def update_table(self,table_name,fields,where_condition):

		self.db_initiate()		



		flen = len(fields)
		temp_field = ''
		ctr = 0
		for i in fields:
			if ctr<flen-1:
				temp_field = temp_field + str(i[0]) + "=" + str(i[1]) + ", "
				ctr = ctr+1
			else:
				temp_field = temp_field + str(i[0]) + "=" + str(i[1])

		full_str = "UPDATE " + config['database'] + '.' + table_name + " SET " + temp_field + " WHERE " + where_condition + ";"

		print (full_str)
		print ("-------------------")
		#for i in values:
		#	print (i)

#		self.cursor.execute(full_str)
#		self.conn.commit()
		try:
			#self.conn.commit()
			self.cursor.execute(full_str)
			self.conn.commit()
			
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))


		self.db_close()


	def db_close(self):
		#---- MySQL CLOSE----#

		#self.conn.commit()
		self.cursor.close()
		self.conn.close ()




#============================================================================#





#---------OPERATIONS---------#

#db_handler1 = DBops()

#db_handler1.db_initiate()
#db_handler1.insert_into("table04", ["id", "name", "value", "remarks"], [34,"test34",442.2,"this is another test entry"])
#db_handler1.db_close()


#db_handler1.update_table("table04",{"name":"Rakshit Agrawal","value":9.3},'''id = 1''')


