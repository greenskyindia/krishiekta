'''

 Parameter 	Description
client_id 	Required. The client ID that you specified when you registered your application with Azure DataMarket.
client_secret 	Required. The client secret value that you obtained when you registered your application with Azure DataMarket.
scope 	Required. Use the URL http://api.microsofttranslator.com as the scope value for the Microsoft Translator API.
grant_type 	Required. Use "client_credentials" as the grant_type value for the Microsoft Translator API. 


"https://datamarket.accesscontrol.windows.net/v2/OAuth2-13"
"https://datamarket.accesscontrol.windows.net/v2/OAuth2-13/"


Client ID - GreenSkyWeather

Client Secret - 4iSklA/UB/VNrglhxbw9tDfq5+bLVgMeH9zriqUI818=

scope - http://api.microsofttranslator.com

grant_type - client_credentials
--------------

b'{"token_type":"http://schemas.xmlsoap.org/ws/2009/11/swt-token-profile-1.0","access_token":"http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fiden
tity%2fclaims%2fnameidentifier=GreenSkyWeather&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https
%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1379158361&Issuer=https%3a%2f%2fdatamarke
t.accesscontrol.windows.net%2f&HMACSHA256=73tI8zo5Z8p1BzhXzEFNQTuQwSpbfrKjjNRtVQZVhLM%3d","expires_in":"599","scope":"http://api.microsofttranslator.c
om"}'






'''


import urllib.parse
import urllib.request
import json
import xml.etree.ElementTree as ET

url = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13/"


values ={	'client_id' : 'GreenSkyWeather',
		'client_secret' : "4iSklA/UB/VNrglhxbw9tDfq5+bLVgMeH9zriqUI818=",
		'scope' : 'http://api.microsofttranslator.com',
		'grant_type' : 'client_credentials'
	}


try:
	data  = urllib.parse.urlencode(values)
	data = data.encode('utf-8')
	req = urllib.request.Request(url, data)
	response = urllib.request.urlopen(req)
	decodedResponse = response.read().decode('utf-8')

	jsonResponse = json.loads(decodedResponse)

	s1 = json.dumps(jsonResponse['access_token'],)
	expiry = json.dumps(jsonResponse['expires_in'])

	x = s1.split('''"''')
	#for i in x:
	#	print (i)

	#print (x)
	oauth = x[1]

	print ("OAuth Token : " + oauth)
	print ("-------------------------------------------")
	print ("Expires In: " + expiry)


	the_page = response.read()
	print(the_page)




except urllib.error.HTTPError as err:
	print("Something went wrong: {}".format(err))






#----Second phase begins for Translate Method


baseurl =  "http://api.microsofttranslator.com/V2/Http.svc/Translate"


token = "Bearer " + oauth



content = "This is a translation test. We are trying to translate text from english to hindi using bing. Please help us translate. We are working from Bangalore. ."


transValues = {	'appId' : token,
		'text' : content,
		'from' : "en",
		'to' : 'hi',
		'contentType' : "text/plain"
		}




#hd  = urllib.parse.urlencode(headers)
#hd = hd.encode('utf-8')
#urllib.request.urlretrieve(business_line, local_dest)
#data = json.dumps(values)

local_dest = 'data001/temptrans'

try:
	parameters  = urllib.parse.urlencode(transValues)
	#data = data.encode('utf-8')
	url = baseurl + "?" + parameters
	#print(url)
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	#urllib.request.urlretrieve(url, local_dest)
	the_page = response.read().decode('utf-8')
	print (the_page)
	

except urllib.error.HTTPError as err:
	print("Something went wrong: {}".format(err))

'''
page_formatted = ET.fromstring(the_page)


transText = page_formatted.text

print(transText)
'''
