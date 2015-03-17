#!/usr/local/bin/python3

#----IMPORTS----#

#--MySQL connector
import mysql.connector

#--Config for DB (ConnTST001)
from db_config03 import config

from Boxes import IdentifierBox

#---- MySQL SELECT----#


class identifier_ops:
	
	db_name = "KEDBTST007"
	db_table = "identifier"


	identifier_obj=IdentifierBox()

	indx = 0
	

	#	DB Initiate

	def db_initiate(self):

		print("We're in the initiator!")
		try:
			self.conn = mysql.connector.connect(**config)
	
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))
        
		self.cursor = self.conn.cursor ()

		self.cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")

		print("Bye Bye Initiator!")





	#	DB Identifier Information 

	def identifier_process(self,identifier_id):
				
		db_identifier_query = "SELECT id, identifier_type, page_type, source_name, value_condition, l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag, l16_tag, l17_tag, l18_tag, l19_tag, l20_tag, attribute, delimiter, recognizer_text, flow_file, last_updated, options FROM " + identifier_ops.db_name + '.' + identifier_ops.db_table + " WHERE id = " + str(identifier_id)  + ';'

		print(db_identifier_query)

		try:
			#self.conn.commit()

			self.cursor.execute(db_identifier_query)

			self.conn.commit()

		except mysql.connector.Error as err:
			print("Something went wrong again: {}".format(err))	

		ctr = 0

		for (id, identifier_type, page_type, source_name, value_condition, l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag, l16_tag, l17_tag, l18_tag, l19_tag, l20_tag, attribute, delimiter, recognizer_text, flow_file, last_updated, options) in self.cursor:
			self.identifier_obj.source_tag_list = [l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag, l16_tag, l17_tag, l18_tag, l19_tag, l20_tag]
			self.identifier_obj.value_condition = value_condition	
			self.identifier_obj.identifier_type = identifier_type
			self.identifier_obj.page_type = page_type
			self.identifier_obj.source_name = source_name
			self.identifier_obj.last_updated = last_updated


		for i in self.identifier_obj.source_tag_list:
			if(i!=None):
				self.indx = self.identifier_obj.source_tag_list.index(i)

		while(len(self.identifier_obj.source_tag_list)>self.indx+1):
			self.identifier_obj.source_tag_list.pop()


		



	#	DB Information Print

	def information_print(self):
		print("Value Condition: " + str(self.identifier_obj.value_condition))
		print("Source Name: " + self.identifier_obj.source_name)
		print("List of Tags: ")
		print(self.identifier_obj.source_tag_list)
		print("___________________________________________________")



	

	#---- MySQL CLOSE----#



	def db_close(self):
		#---- MySQL CLOSE----#

		#self.conn.commit()
		self.cursor.close ()

		#New component
		self.conn.cmd_quit()

		self.conn.close ()



	#	Identifier API function


	def identifier_information(self, ident_id):
		self.db_initiate()
		self.identifier_process(ident_id)
		self.db_close()	
		
		return self.identifier_obj








#============================================================================#





#---------OPERATIONS---------#

'''

x = identifier_ops()

x.db_initiate()
x.identifier_process('57')
x.information_print()
x.identifier_process('7')
x.information_print()
x.identifier_process('5')
x.information_print()
x.db_close()
'''
