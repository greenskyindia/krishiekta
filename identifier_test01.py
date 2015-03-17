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


conn.commit()
#---- MySQL SELECT----#

full_str = '''SELECT id, identifier_type, page_type, source_name, l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag FROM KEDBTST002.identifier WHERE identifier_type = 'content';'''


cursor.execute(full_str)

#conn.commit()


print(cursor)



ctr = 0
for (id, identifier_type, page_type, source_name, l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag) in cursor:
	tlist = [l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag]	
	#ctr = ctr +1	
	
	print("ID: {}, Type: {} for Page {} of Source: {}, \n\tTags 2: {}, 6: {}, 8 {}, 9: {}, 10: {}, 11: {}".format(id, identifier_type, page_type, source_name, l1_tag, l2_tag, l3_tag, l4_tag, l5_tag, l6_tag, l7_tag, l8_tag, l9_tag, l10_tag, l11_tag, l12_tag, l13_tag, l14_tag, l15_tag))

print("Tag list = ", tlist, "\n\n")



for i in tlist:
	if(i!=None):
		print (len(tlist))
		print(tlist)
		print(i,":",tlist.index(i))
		#del (i)
		#tlist.pop()
		indx = tlist.index(i)

while(len(tlist)>indx+1):
	tlist.pop()

print (len(tlist))
print(tlist)
#---- MySQL CLOSE----#



#conn.commit()
cursor.close ()
conn.close ()




#============================================================================#





#---------OPERATIONS---------#

#db_handler1 = DBops()

#db_handler1.insert_into("table04", ["id", "name", "value", "remarks"], [2,"test2",4.2,"this is second test entry"])

#db_handler1.update_table("table04",{"name":"Rakshit Agrawal","value":9.3},'''id = 1''')


