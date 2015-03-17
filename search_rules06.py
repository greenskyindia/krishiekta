#!/usr/local/bin/python3

#--------------IMPORTS-------------#


#--MySQL connector
import mysql.connector


#--Config for DB (KEDBTST007)
from db_config03 import config

import time


#--URLLIB
import urllib.request


from parsing_engine01 import ParsingEngine
from identifier_test04 import identifier_ops

from Boxes import RawDataBox, SourceBox, IdentifierBox

from dbtest05 import DBops

#source_tag_list, val_condition


#------------CLASSES-------------#



#----------SEARCH FUNCTIONS--------#



class SearchRules:

	FinalData = ''
	
	get_identifier_info = identifier_ops()

	#identifier_object = get_identifier_info.identifier_information()
	
	#SourceTagList = identifier_object.source_tag_list

	Identifiers = ['content','keywords','location','image']

	#ListLength = len(SourceTagList)

	source_info = SourceBox(0)

	article_list = []
	ctr = 0

	db_handler = DBops()

	db_table = "raw_data"
	src_db_table = "source"
	db_name = "KEDBTST007"



	#------DB Initiate

	def db_initiate(self):

		print("We're in the DB initiator!")
		try:
			self.conn = mysql.connector.connect(**config)
	
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))
        
		self.cursor = self.conn.cursor()

		#self.cursor.execute ("SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'")

		print("Bye Bye Initiator!")





	def db_close(self):
		#---- MySQL CLOSE----#

		#self.conn.commit()
		#time.sleep(5) # Time delay
		print("---In DB close")
		self.cursor.close()

		x = self.conn.is_connected()
		print("!!!!MySQL conncection before Close: "+ str(x))

		self.conn.cmd_quit()
		self.conn.close()
		
		print("--DB close performed")

		x = self.conn.is_connected()
		print("!!!!MySQL conncection After Close: "+ str(x))






	def raw_data_table_fetch(self):

		self.db_initiate()
						
		rd_query = "SELECT " + "id, uid, source_id, url, date, date_string, location, title, content, tags, keywords, image, video, audio, related, cge_ready, error_check, category1, wt_cat1, category2, wt_cat2, category3, wt_cat3, crop1, wt_crop1, crop2, wt_crop2" + " FROM " + SearchRules.db_name + '.' + SearchRules.db_table + " WHERE " "content=" + '"temp"' + ";"



		print(rd_query)



		try:
			#self.conn.commit()

			self.cursor.execute(rd_query)

			self.conn.commit()

		except mysql.connector.Error as err:
			print("Something went wrong again: {}".format(err))	

		

		for (id, uid, source_id, url, date, date_string, location, title, content, tags, keywords, image, video, audio, related, cge_ready, error_check, category1, wt_cat1, category2, wt_cat2, category3, wt_cat3, crop1, wt_crop1, crop2, wt_crop2) in self.cursor:
			

			self.article_list.append(RawDataBox(self.ctr))
			self.ctr = self.ctr + 1
			

			self.article_list[-1].raw_data_id = id

			self.article_list[-1].uid = uid
			self.article_list[-1].source_id = source_id
			
			self.article_list[-1].url = url
			self.article_list[-1].date = date
			self.article_list[-1].date_string = date_string

			self.article_list[-1].page_data['location'] = location
			self.article_list[-1].page_data['title'] = title
			self.article_list[-1].page_data['content'] = content
			self.article_list[-1].page_data['tags'] = tags
			self.article_list[-1].page_data['keywords'] = keywords
			self.article_list[-1].page_data['image'] = image
			self.article_list[-1].page_data['video'] = video
			self.article_list[-1].page_data['audio'] = audio
			self.article_list[-1].page_data['related'] = related

			'''
			
			self.article_list[-1].location = location
			self.article_list[-1].title = title
			self.article_list[-1].content = content
			self.article_list[-1].tags = tags
			self.article_list[-1].keywords = keywords
			self.article_list[-1].image = image
			self.article_list[-1].video = video
			self.article_list[-1].audio = audio
			self.article_list[-1].related = related

			'''

			self.article_list[-1].cge_ready = cge_ready

			self.article_list[-1].error_check = error_check

			self.article_list[-1].category1 = category1
			self.article_list[-1].wt_cat1 = wt_cat1
			self.article_list[-1].category2 = category2
			self.article_list[-1].wt_cat2 = wt_cat2
			self.article_list[-1].category3 = category3
			self.article_list[-1].wt_cat3 = wt_cat3

			self.article_list[-1].crop1 = crop1
			self.article_list[-1].wt_crop1 = wt_crop1
			self.article_list[-1].crop2 = crop2
			self.article_list[-1].wt_crop2 = wt_crop2
			
		self.db_close()




	def source_id_fetch(self, src_id):


		self.db_initiate()

		source_query = "SELECT " + "id, name, url, short_name, information, language, gen_page_type, date_format, last_fetch_date, 	last_base_date, gen_date_id, gen_title_id, gen_url_id, spec_date_id, spec_title_id, spec_url_id, spec_content_id, spec_location_id, spec_tag_id, spec_keyword_id, spec_image_id, spec_video_id, spec_audio_id, spec_related_id, category1, weight_cat1, category2, weight_cat2, category3, weight_cat3 " + " FROM " + SearchRules.db_name + '.' + SearchRules.src_db_table  + " WHERE id = " + str(src_id)  + ';'



		print(source_query)



		try:
			#self.conn.commit()

			self.cursor.execute(source_query)

			self.conn.commit()

		except mysql.connector.Error as err:
			print("Something went wrong again: {}".format(err))	

		

		for (id, name, url, short_name, information, language, gen_page_type, date_format, last_fetch_date, last_base_date, gen_date_id, gen_title_id, gen_url_id, spec_date_id, spec_title_id, spec_url_id, spec_content_id, spec_location_id, spec_tag_id, spec_keyword_id, spec_image_id, spec_video_id, spec_audio_id, spec_related_id, category1, weight_cat1, category2, weight_cat2, category3, weight_cat3) in self.cursor:
			

			self.source_info.source_id = id
			self.source_info.name = name
			self.source_info.url = url
			self.source_info.short_name = short_name
			self.source_info.information = information
			self.source_info.language = language
			self.source_info.gen_page_type = gen_page_type
			self.source_info.date_format = date_format
			self.source_info.last_fetch_date = last_fetch_date
			self.source_info.last_base_date = last_base_date
	
			self.source_info.gen_tag_list['date']= gen_date_id
			self.source_info.gen_tag_list['title']= gen_title_id
			self.source_info.gen_tag_list['url']= gen_url_id

			self.source_info.spec_tag_list['date']= spec_date_id
			self.source_info.spec_tag_list['title']= spec_title_id
			self.source_info.spec_tag_list['url']= spec_url_id
			self.source_info.spec_tag_list['content']= spec_content_id
			self.source_info.spec_tag_list['location']= spec_location_id
			self.source_info.spec_tag_list['tag']= spec_tag_id
			self.source_info.spec_tag_list['keywords']= spec_keyword_id
			self.source_info.spec_tag_list['image']= spec_image_id
			self.source_info.spec_tag_list['video']= spec_video_id
			self.source_info.spec_tag_list['audio']= spec_audio_id
			self.source_info.spec_tag_list['related']= spec_related_id

			self.source_info.category1 = category1
			self.source_info.weight_cat1 = weight_cat1
			self.source_info.category2 = category2
			self.source_info.weight_cat2 = weight_cat2
			self.source_info.category3 = category3
			self.source_info.weight_cat3 = weight_cat3	

		self.db_close()

		return self.source_info

		





	def search_processor(self):
	
		#self.db_initiate()
		print("Processor starts")

		self.raw_data_table_fetch()

		for i in self.article_list:
			s_info = self.source_id_fetch(i.source_id)

			update_dict = []
			
			for j in SearchRules.Identifiers:

				

				ident_temp = self.get_identifier_info.identifier_information(s_info.spec_tag_list[j])
				print("\n\tValue condition")
				print(ident_temp.value_condition)

				#try:

				#print("\n\tValue condition" + ident_temp.value_condition)

				if ident_temp.value_condition == 0:
					i.page_data[j] = self.search_fn0(i.uid, i.url, ident_temp.source_tag_list)


				elif ident_temp.value_condition == 1:
					i.page_data[j] = self.search_fn1(i.uid, i.url, ident_temp.source_tag_list, ident_temp.attribute)


				elif ident_temp.value_condition == 2:
					i.page_data[j] = self.search_fn2(i.uid, i.url, ident_temp.source_tag_list)


				elif ident_temp.value_condition == 3:
					i.page_data[j] = self.search_fn3(i.uid, i.url, ident_temp.source_tag_list, ident_temp.delimiter)

				else:
					print("Reached else")


				text = '"' + str(i.page_data[j]) + '"'
				update_dict.append((j,text))
				print (update_dict)

#				except:

				#print("Error as the identifier doesn't exist")

			#At this point, article_list should have all items with their data updated. Now it needs to be pushed into the database

			# UPDATE RAW_DATA with all entries

			print(update_dict)

			where_string = "id = " + str(i.raw_data_id)

			self.db_handler.update_table("raw_data", update_dict, where_string)

			del update_dict	

			'''
			self.conn.commit()
			self.cursor.close()
			self.conn.close ()
			'''



	#------Search Function 0 - For case with only last tag's data

	def search_fn0(self,art_uid, art_url, src_tag_list):
		print("\n*** In function 0")

		FinalData = ''

		num = 0
		
		parser = ParsingEngine()

		local_filename = "data003/" + art_uid + "." + 'html'

		urllib.request.urlretrieve(art_url, local_filename)

		f = open(local_filename,'r')

		parser.feed(f.read())

		f.close()

		Tree = parser.PageTree

		i = 0
		
		ListLength = len(src_tag_list)

		temp = Tree[i]

		try:	
			while (num <= ListLength+1):
				if(src_tag_list[num] == temp.tcombined_name):
					for j in temp.tchild:
						if(Tree[j].tcombined_name == src_tag_list[num+1]):
							f = Tree[j].tid
							temp = Tree[f]
							if(num == ListLength-2):
								FinalData = FinalData + " " + temp.tdata
					num = num + 1
	
	
		except:
			print ("\n\nData : " + FinalData)
	
		

		return FinalData


	


	#------Search Function 1 - For case with last tag's attribute value

	def search_fn1(self,art_uid, art_url, src_tag_list, attr):
		print("\n*** In function 1")
		FinalData = ''

		num = 0
		
		parser = ParsingEngine()

		local_filename = "data003/" + art_uid + "." + 'html'

		urllib.request.urlretrieve(art_url, local_filename)

		f = open(local_filename,'r')

		parser.feed(f.read())

		f.close()


		Tree = parser.PageTree

		i = 0
		
		ListLength = len(src_tag_list)

		temp = Tree[i]

		try:	
			while (num <= ListLength+1):
				if(src_tag_list[num] == temp.tcombined_name):
					for j in temp.tchild:
						if(Tree[j].tcombined_name == src_tag_list[num+1]):
							f = Tree[j].tid
							temp = Tree[f]
							if(num == ListLength-2):
								FinalData = temp.tattrib[attr]
					num = num + 1
	
	
		except:
			print ("\n\nData : " + FinalData)
	
		return FinalData


		




	#------Search Function 2 - For case with last and second last tag's data

	def search_fn2(self,art_uid, art_url, src_tag_list):
		print("\n*** In function 2")
		FinalData = ''

		num = 0
		
		parser = ParsingEngine()

		local_filename = "data003/" + art_uid + "." + 'html'

		urllib.request.urlretrieve(art_url, local_filename)

		f = open(local_filename,'r')

		parser.feed(f.read())

		f.close()


		Tree = parser.PageTree

		i = 0
		
		ListLength = len(src_tag_list)

		temp = Tree[i]

		try:	
			while (num <= ListLength+1):
				if(src_tag_list[num] == temp.tcombined_name):
					for j in temp.tchild:
						if(Tree[j].tcombined_name == src_tag_list[num+1]):
							f = Tree[j].tid
							temp = Tree[f]
							if(num >= ListLength-3):
								FinalData = FinalData + " " + temp.tdata
					num = num + 1
	
	
		except:
			print ("\n\nData : " + FinalData)
	
		return FinalData




	#------Search Function 3 - For case with last tag with delimiter

	def search_fn3(self,art_uid, art_url, src_tag_list, delimiter):
		print("\n*** In function 3")
		EndString = ''
		FinalData = ''

		num = 0
		
		parser = ParsingEngine()

		local_filename = "data003/" + art_uid + "." + 'html'

		urllib.request.urlretrieve(art_url, local_filename)

		f = open(local_filename,'r')

		parser.feed(f.read())

		f.close()


		Tree = parser.PageTree

		i = 0
		
		ListLength = len(src_tag_list)

		temp = Tree[i]

		try:	
			while (num <= ListLength+1):
				if(src_tag_list[num] == temp.tcombined_name):
					for j in temp.tchild:
						if(Tree[j].tcombined_name == src_tag_list[num+1]):
							f = Tree[j].tid
							temp = Tree[f]
							if(num == ListLength-2):
								EndString = EndString + " " + temp.tdata
					num = num + 1
	
	
		except:
			print ("\n\nData : " + FinalData)

		try:
			split_text = EndString.split(delimiter)
			FinalData = split_text[0]
		except:
			FinalData = EndString
	
		return FinalData






	'''
	def search_bl(self,Tree):
		num = 0
		i = 0
		temp = Tree[i]

#		if(val_condition

		try:	
			while (num <= SearchRules.ListLength+1):
				if(SearchRules.SourceTagList[num] == temp.tcombined_name):
					for j in temp.tchild:
						if(Tree[j].tcombined_name == SearchRules.SourceTagList[num+1]):
							f = Tree[j].tid
							temp = Tree[f]
							if(num == SearchRules.ListLength-2):
								SearchRules.FinalData = SearchRules.FinalData + " " + temp.tdata
					num = num + 1
	
	
		except:
			print ("\n\nData : " + SearchRules.FinalData)
	



	def search_02(self,Tree):
		num = 0
		i = 0
		temp = Tree[i]

#		if(val_condition

		try:	
			while (num <= SearchRules.ListLength+1):

				if(SearchRules.SourceTagList[num] == temp.tcombined_name):

					for j in temp.tchild:

						if(Tree[j].tcombined_name == SearchRules.SourceTagList[num+1]):

							f = Tree[j].tid
							temp = Tree[f]

							if(num == SearchRules.ListLength-2):
								SearchRules.FinalData = SearchRules.FinalData + " " + temp.tdata
					num = num + 1
	
	
		except:
			print ("\n\nData : " + SearchRules.FinalData)
	
	
	'''




	
#---------OPERATIONS---------#
	


searcher = SearchRules()

print("code begins")

searcher.search_processor()
print("****************************************************")


