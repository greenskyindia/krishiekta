#!/usr/local/bin/python3

#------- Boxes.py -------#


#-------------------------------------------------------------------------------#
#- This file contains box classes for all Database tables. 
#- Any use of class object representing a database table should use this file.
#-------------------------------------------------------------------------------#


#--------Source Table-------#


class SourceBox:

	counter = 0
	indx = None

	source_id = 0
	name = ''
	url = ''
	short_name = ''
	information = ''
	language = ''
	gen_page_type = ''
	date_format = ''
	last_fetch_date = ''
	last_base_date = ''
	gen_tag_list = dict(date=None,title=None,url=None)

	#	gen_date_id = 0
	#	gen_title_id = 0
	#	gen_url_id = 0

	spec_tag_list = dict(date=None, title=None, url=None, content=None, location=None, tag=None, keyword=None, image=None, video=None, audio=None, related=None)

	#	spec_date_id = 0
	#	spec_title_id = 0
	#	spec_url_id = 0
	#	spec_content_id = 0
	#	spec_location_id = 0
	#	spec_tag_id = 0
	#	spec_keyword_id = 0
	#	spec_image_id = 0
	#	spec_video_id = 0
	#	spec_audio_id = 0
	#	spec_related_id = 0

	category1 = ''
	weight_cat1 = 0.0
	category2 = ''
	weight_cat2 = 0.0
	category3 = ''
	weight_cat3 = 0.0	


	def __init__(self,val):
		self.indx = val
		self.gen_tag_list = {}
		self.spec_tag_list = {}
		SourceBox.counter = SourceBox.counter + 1


#--------Identifier Table-------#


class IdentifierBox:

	counter = 0
	indx = None

	identifier_id = 0
	identifier_type = ''
	page_type = ''
	source_name = ''
	value_condition = 0
	parsing_type = ''
	source_tag_list = []
	attribute = ''
	delimiter = ''
	recognizer_text = ''
	flow_file = ''
	options = ''
	error_check = ''


	def __init__(self):
		#self.indx = val
		self.source_tag_list = []
		#self.spec_tag_list = []
		IdentifierBox.counter = IdentifierBox.counter + 1


#--------Raw Data Table-------#


class RawDataBox:

	counter = 0
	indx = None

	raw_data_id = 0
	uid = 0
	source_id = 0
	url = ''
	date = ''
	date_string = ''
	page_data = []
	#location = ''
	#title = ''
	#content = ''
	#tags = ''
	#keywords = ''
	#image = ''
	#video = ''
	#audio = ''
	#related	= ''
	error_check = 0
	category1 = 0
	wt_cat1 = 0.0
	category2 = 0
	wt_cat2 = 0.0
	category3 = 0
	wt_cat3 = 0.0
	crop1 = 0
	wt_crop1 = 0.0
	crop2 = 0
	wt_crop2 = 0.0
	cge_ready = 0


	def __init__(self,val):
		self.indx = val
		self.page_data = {}
		RawDataBox.counter = RawDataBox.counter + 1


#--------Final Data Table-------#


class FinalDataBox:

	counter = 0
	indx = None

	final_data_id = 0
	rd_id = 0
	source_id = 0
	sms_text = ''
	tweet = ''
	facebook_post = ''
	mail_text = ''
	wordpress_post = ''
	scribd_article = ''
	outpu_tags = ''
	sms_count = 0
	tweet_count = 0
	facebook_count = 0
	mail_push_count = 0
	wordpress_count = 0
	scribd_count = 0
	misc_count = 0
	extra = ''


	def __init__(self,val):
		self.indx = val
		FinalDataBox.counter = FinalDataBox.counter + 1





