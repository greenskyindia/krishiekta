

'''

http://api.microsofttranslator.com/V2/Http.svc/Translate


SITE ID information

b'{
"token_type":"http://schemas.xmlsoap.org/ws/2009/11/swt-token-profile-1.0",
"access_token":"http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fidentity%2fclaims%2fnameidentifier=GreenSkyWeather&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1378755491&Issuer=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&HMACSHA256=QWyPKnyVcGgv8MjBFFhB3rgOPewBLOT5V9SUOC7xgmE%3d",
"expires_in":"600",
"scope":"http://api.microsofttranslator.com"}'

'''


import urllib.request
import urllib.parse
import json

url = 'http://api.microsofttranslator.com/V2/Http.svc/GetTranslations'

oauth = "http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fidentity%2fclaims%2fnameidentifier=GreenSkyWeather&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1378755491&Issuer=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&HMACSHA256=QWyPKnyVcGgv8MjBFFhB3rgOPewBLOT5V9SUOC7xgmE%3d"

token = "Bearer " + oauth

headers = {	'authorization': token,
		'Content-Type':'application/x-www-form-urlencoded'
	  }

values ={	'appId' : '',
		'text' : 'This is a simple english sentence. This sentence has to be translated now.',
		'from' : "en",
		'to' : 'hi',
		'maxTranslations' : 10
	}

#hd  = urllib.parse.urlencode(headers)
#hd = hd.encode('utf-8')

#data = json.dumps(values)

try:
	data  = urllib.parse.urlencode(values)
	data = data.encode('utf-8')
	req = urllib.request.Request(url, data, headers)
	response = urllib.request.urlopen(req)

	the_page = response.read()
	print (the_page)
	

except urllib.error.HTTPError as err:
	print("Something went wrong: {}".format(err))

