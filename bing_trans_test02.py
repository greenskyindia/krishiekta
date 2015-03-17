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

url = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13/"


values ={	'client_id' : 'GreenSkyWeather',
		'client_secret' : "4iSklA/UB/VNrglhxbw9tDfq5+bLVgMeH9zriqUI818=",
		'scope' : 'http://api.microsofttranslator.com',
		'grant_type' : 'client_credentials'
	}


data  = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page)






'''


b'{
"token_type":"http://schemas.xmlsoap.org/ws/2009/11/swt-token-profile-1.0",
"access_token":"http%3a%2f%2fschemas.xmlsoap.org%2fws%2f2005%2f05%2fidentity%2fclaims%2fnameidentifier=GreenSkyWeather&http%3a%2f%2fschemas.microsoft.com%2faccesscontrolservice%2f2010%2f07%2fclaims%2fidentityprovider=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&Audience=http%3a%2f%2fapi.microsofttranslator.com&ExpiresOn=1378755491&Issuer=https%3a%2f%2fdatamarket.accesscontrol.windows.net%2f&HMACSHA256=QWyPKnyVcGgv8MjBFFhB3rgOPewBLOT5V9SUOC7xgmE%3d",
"expires_in":"600",
"scope":"http://api.microsofttranslator.com"}'


'''
