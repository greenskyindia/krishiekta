#!/usr/local/bin/python3

import subprocess
import urllib.request
import json
import datetime
import sys

url = 'http://api.microsofttranslator.com/V2/Http.svc/Translate'


''' Auth Data

Primary Account Key 	FzNO+RgpXHtQV8nV5x3t+n4XJRdWzZqSW0k1JN41sJI
Customer ID 	53a475ac-a49f-4ff1-872c-5bb8c254bd21

'''


#headers

trans_head =	{
			"appId": "0.1"
			,"text": "This is first text message. Please translate it."
			,"from": "0.1"
			,"to": "0.1"
			,"contentType": "text/plain"
			,"category": "general"
		}




#string uri = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text=" + System.Web.HttpUtility.UrlEncode(text) + "&from=" + from + "&to=" + to;

local_file = 'data001/blgen002.xml'

#f = urllib.request.urlopen(url) 

urllib.request.urlretrieve(url, local_file)

#print headers

