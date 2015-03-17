##########################################################
#----------------GET Request----------------------------#
#########################################################

import urllib.request
import urllib.parse
import json

'''

Things to be specified:

OAUTH Token for Header

URL
Parameters to be appended onto URL

'''


baseurl =  "http://api.microsofttranslator.com/V2/Http.svc/Translate"

'''
oauth = "http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fidentity%2fclaims%2fnameidentifier=GreenSkyWeather&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1378755491&Issuer=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&HMACSHA256=QWyPKnyVcGgv8MjBFFhB3rgOPewBLOT5V9SUOC7xgmE%3d"
'''

oauth = "http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fidentity%2fclaims%2fnameidentifier=GreenSkyWeather&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1379158361&Issuer=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&HMACSHA256=73tI8zo5Z8p1BzhXzEFNQTuQwSpbfrKjjNRtVQZVhLM%3d"

token = "Bearer " + oauth

headers = {	'authorization': token,
		'Content-Type':'application/x-www-form-urlencoded'
	  }

values ={	'appId' : token,
		'text' : "This is a simple english sentence. This sentence has to be translated now.",
		'from' : "en",
		'to' : 'hi',
		'contentType' : "text/plain"
	}




#hd  = urllib.parse.urlencode(headers)
#hd = hd.encode('utf-8')
#urllib.request.urlretrieve(business_line, local_dest)
#data = json.dumps(values)

local_file = 'data001/bingout'

try:
	parameters  = urllib.parse.urlencode(values)
	#data = data.encode('utf-8')
	url = baseurl + "?" + parameters
	#print(url)
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	the_page = response.read().decode('utf-8')
	print (the_page)
	

except urllib.error.HTTPError as err:
	print("Something went wrong: {}".format(err))

