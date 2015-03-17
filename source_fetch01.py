#!/usr/local/bin/python3

#----IMPORTS----#


#--MySQL connector
import mysql.connector


#--Config for DB (KEDBTST006)
from db_config03 import config


#--URLLIB
import urllib.request

#--XML
import xml.etree.ElementTree as ET


#--DATETIME
from datetime import datetime



from source_box01 import SourceBox
from identifier_test04 import identifier_ops
from dbtest03 import DBops


#---- MySQL SELECT----#


class source_ops:
	
	db_name = "KEDBTST006"
	db_table = "source"

	identifier_operator = identifier_ops()

	source_list = []
	ctr = 0
	flag=0

	db_handler = DBops()


	
	def db_initiate(self):

		print("We're in the initiator!")
		try:
			self.conn = mysql.connector.connect(**config)
	
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))
        
		self.cursor = self.conn.cursor ()

		self.cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")

		print("Bye Bye Initiator!")







	def source_table_fetch(self):
						
		source_query = "SELECT " + "id, name, url, short_name, information, language, gen_page_type, last_fetch_date, last_base_date, gen_date_id, gen_title_id, gen_url_id, spec_date_id, spec_title_id, spec_url_id, spec_content_id, spec_location_id, spec_tag_id, spec_keyword_id, spec_image_id, spec_video_id, spec_audio_id, spec_related_id, category1, weight_cat1, category2, weight_cat2, category3, weight_cat3 " + "FROM " + source_ops.db_name + '.' + source_ops.db_table + ";"



		print(source_query)



		try:
			self.conn.commit()

			self.cursor.execute(source_query)

			self.conn.commit()

		except mysql.connector.Error as err:
			print("Something went wrong again: {}".format(err))	

		

		for (id, name, url, short_name, information, language, gen_page_type, date_format, last_fetch_date, last_base_date, gen_date_id, gen_title_id, gen_url_id, spec_date_id, spec_title_id, spec_url_id, spec_content_id, spec_location_id, spec_tag_id, spec_keyword_id, spec_image_id, spec_video_id, spec_audio_id, spec_related_id, category1, weight_cat1, category2, weight_cat2, category3, weight_cat3) in self.cursor:
			

			self.source_list.append(SourceBox(self.ctr))
			self.ctr = self.ctr + 1
			

			self.source_list[-1].source_id = id
			self.source_list[-1].name = name
			self.source_list[-1].url = url
			self.source_list[-1].short_name = short_name
			self.source_list[-1].information = information
			self.source_list[-1].language = language
			self.source_list[-1].gen_page_type = gen_page_type
			self.source_list[-1].date_format = date_format
			self.source_list[-1].last_fetch_date = last_fetch_date
			self.source_list[-1].last_base_date = last_base_date
	
			self.source_list[-1].gen_tag_list['date']= gen_date_id
			self.source_list[-1].gen_tag_list['title']= gen_title_id
			self.source_list[-1].gen_tag_list['url']= gen_url_id

			self.source_list[-1].spec_tag_list['date']= spec_date_id
			self.source_list[-1].spec_tag_list['title']= spec_title_id
			self.source_list[-1].spec_tag_list['url']= spec_url_id
			self.source_list[-1].spec_tag_list['content']= spec_content_id
			self.source_list[-1].spec_tag_list['location']= spec_location_id
			self.source_list[-1].spec_tag_list['tag']= spec_tag_id
			self.source_list[-1].spec_tag_list['keyword']= spec_keyword_id
			self.source_list[-1].spec_tag_list['image']= spec_image_id
			self.source_list[-1].spec_tag_list['video']= spec_video_id
			self.source_list[-1].spec_tag_list['audio']= spec_audio_id
			self.source_list[-1].spec_tag_list['related']= spec_related_id

			self.source_list[-1].category1 = category1
			self.source_list[-1].weight_cat1 = weight_cat1
			self.source_list[-1].category2 = category2
			self.source_list[-1].weight_cat2 = weight_cat2
			self.source_list[-1].category3 = category3
			self.source_list[-1].weight_cat3 = weight_cat3			


			print(self.source_list[-1].gen_tag_list)





	def source_print(self):
		for i in self.source_list:
			#print(i.ctr)
			print(i.indx)
			print(i.source_id)
			print(i.name)
			print(i.url)
			print(i.spec_tag_list['title'])
			print("___________________________________________________")








	def article_collection(self):
		for i in self.source_list:
			if(i.gen_page_type == 'XML'):
				source_ops.flag=0
				self.general_parser_xml(i.indx)
			elif(i.gen_page_type == 'HTML'):
				self.general_parser_html(i.indx)











	def general_parser_xml(self,src_indx):
		print(self.source_list[src_indx].gen_tag_list['title'])
		print(self.source_list[src_indx].gen_tag_list['date'])
		print(self.source_list[src_indx].gen_tag_list['url'])
		print(self.source_list[src_indx].gen_tag_list)

		print(self.source_list[src_indx].spec_tag_list)		
		print(self.source_list[src_indx].spec_tag_list['content'])
		print(self.source_list[src_indx].spec_tag_list['title'])
		print(self.source_list[src_indx].spec_tag_list['image'])
		print(self.source_list[src_indx].spec_tag_list['keyword'])
		print(self.source_list[src_indx].name + self.source_list[src_indx].url)


		if(self.source_list[src_indx].gen_tag_list['url']!=None):
			print("Inside")
			datetime_now = datetime.now()
			datetime_str = datetime_now.strftime("_%d%b%Y_%Hh_%Mmin")
			extn = self.source_list[src_indx].gen_page_type.lower()
			local_filename = "data002/" + self.source_list[src_indx].short_name + datetime_str + "." + extn

			urllib.request.urlretrieve(self.source_list[src_indx].url, local_filename)

			#fetch identifier list


			art_list = []
	
			for var in ['title','date','url']:

				ident_holder = self.identifier_operator.identifier_information(self.source_list[src_indx].gen_tag_list[var])
				ident_list = ident_holder.source_tag_list

				list_str = "."

				for i in ident_list:
					list_str = list_str + "/" + i

				
				tree = ET.parse(local_filename)
				root = tree.getroot()

				temp = root.findall(list_str)
				ctr = 0
				for j in temp:
					if source_ops.flag==0:
						art_list.append({'title':None,'url':None,'date':None})
						
					art_list[ctr][var]=j.text
					ctr = ctr+1

				source_ops.flag=1

			uid_val = 500

			for i in art_list:
				#uid_val = UID_creator.generate()
				#bl_time_format = "%a, %d %b %Y %H:%M:%S +0530"

				temp_date = datetime.strptime(i['date'], self.source_list[src_indx].date_format)


				uid_val = uid_val+10
				temp_list = [uid_val,self.source_list[src_indx].source_id, i['url'],temp_date,i['title'],"temp",0]

#				tdate = datetime.st

#				tdate = datetime.strptime("Sat, 21 Aug 2013 02:02:15 ", "%a, %d %b %Y %H:%M:%S ")
#				odate2 = odate.strftime("%a, %d %b %Y %H:%M:%S ")

				tdate = self.source_list[src_indx].last_fetch_date.strftime("%a, %d %b %Y %H:%M:%S ")




				print(i['date'])
				print(tdate)
				if i['date']<tdate:
					print("\t\t\t#####Date Value satisfied")
					self.db_handler.insert_into("KEDBTST006.raw_data",["uid","source_id","url","date","title","content","cge_ready"],temp_list)


			print (local_filename)

			#for i in self.source_list[src_indx].gen_tag_list:
			







		

	def general_parser_html(self,src_indx):
		print(self.source_list[src_indx].name)
		print(self.source_list[src_indx].gen_tag_list['title'])
		print(self.source_list[src_indx].spec_tag_list['content'])
		print(self.source_list[src_indx].spec_tag_list['title'])
		print(self.source_list[src_indx].spec_tag_list['image'])
		print(self.source_list[src_indx].spec_tag_list['keyword'])
		print(self.source_list[src_indx].name + self.source_list[src_indx].url)

		datetime_now = datetime.now()
		datetime_str = datetime_now.strftime("_%d%b%Y_%H_%M")
		extn = self.source_list[src_indx].gen_page_type.lower()
		local_filename = self.source_list[src_indx].short_name + datetime_str + "." + extn

		print (local_filename)


	




	#---- MySQL CLOSE----#



	def db_close(self):
		#---- MySQL CLOSE----#

		self.conn.commit()
		self.cursor.close ()
		self.conn.close ()




#============================================================================#





#---------OPERATIONS---------#



x = source_ops()

x.db_initiate()
x.source_table_fetch()
x.db_close()
#x.source_print()
x.article_collection()

