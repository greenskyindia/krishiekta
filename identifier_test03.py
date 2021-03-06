#!/usr/local/bin/python3

#----IMPORTS----#

#--MySQL connector
import mysql.connector

#--Config for DB (ConnTST001)
from db_config03 import config


#---- MySQL SELECT----#


class identifier_ops:
	
	db_name = "KEDBTST006"
	db_table = "identifier"


	source_tag_list = []
	val_condition = ''
	pg_type = ''
	src_name = ''
	lst_updated = None
	indx = 0

	
	def db_initiate(self):

		print("We're in the initiator!")
		try:
			self.conn = mysql.connector.connect(**config)
	
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))
        
		self.cursor = self.conn.cursor ()

		self.cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")

		print("Bye Bye Initiator!")


	def identifier_information(self,required_identifier):
				
		db_identifier_query = "SELECT id, identifier_type, page_type, source_name, value_condition, l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag, l16_tag, l17_tag, l18_tag, l19_tag, l20_tag, attribute, delimiter, recognizer_text, flow_file, last_updated, options FROM " + identifier_ops.db_name + '.' + identifier_ops.db_table + " WHERE identifier_type = " + "'"+ required_identifier + "'" + ';'

		print(db_identifier_query)

		try:
			#self.conn.commit()

			self.cursor.execute(db_identifier_query)

			self.conn.commit()

		except mysql.connector.Error as err:
			print("Something went wrong again: {}".format(err))	

		ctr = 0

		for (id, identifier_type, page_type, source_name, value_condition, l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag, l16_tag, l17_tag, l18_tag, l19_tag, l20_tag, attribute, delimiter, recognizer_text, flow_file, last_updated, options) in self.cursor:
			self.source_tag_list = [l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag, l16_tag, l17_tag, l18_tag, l19_tag, l20_tag]
			self.val_condition = value_condition	
			self.id_type = identifier_type
			self.page_type = page_type
			self.src_name = source_name
			self.lst_updated = last_updated


		for i in self.source_tag_list:
			if(i!=None):
				self.indx = self.source_tag_list.index(i)

		while(len(self.source_tag_list)>self.indx+1):
			self.source_tag_list.pop()


	def information_print(self):
		print("Value Condition: " + str(self.val_condition))
		print("Source Name: " + self.src_name)
		print("List of Tags: ")
		print(self.source_tag_list)
		print("___________________________________________________")



#---- MySQL CLOSE----#



	def db_close(self):
		#---- MySQL CLOSE----#

		self.conn.commit()
		self.cursor.close ()
		self.conn.close ()




#============================================================================#





#---------OPERATIONS---------#



x = identifier_ops()

x.db_initiate()
x.identifier_information('title')
x.db_close()
x.information_print()

