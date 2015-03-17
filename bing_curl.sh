curl \
-H 'authorization: Bearer http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fidentity%2fclaims%2fnameidentifier=GreenSkyWeather&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1378755491&Issuer=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&HMACSHA256=QWyPKnyVcGgv8MjBFFhB3rgOPewBLOT5V9SUOC7xgmE%3d' \
--data-urlencode 'appId=' \
--data-urlencode 'text=This is a simple english sentence. This sentence has to be translated now.' \
--data-urlencode 'from=en' \
--data-urlencode 'to=DE' \
--data-urlencode 'contentType=text/plain' \
--data-urlencode 'category=general' \
'http://api.microsofttranslator.com/V2/Http.svc/Translate'





url = 'http://api.microsofttranslator.com/V2/Http.svc/Translate'

oauth = "http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fidentity%2fclaims%2fnameidentifier=GreenSkyWeather&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1378755491&Issuer=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&HMACSHA256=QWyPKnyVcGgv8MjBFFhB3rgOPewBLOT5V9SUOC7xgmE%3d"

token = "Bearer " + oauth

headers = {	'authorization': token
	  }

values ={	'appId' : '',
		'text' : 'This is a simple english sentence. This sentence has to be translated now.',
		'from' : 'en',
		'to' : 'hi',
		'contentType' : 'text/plain',
		'category' : 'general'
	}

