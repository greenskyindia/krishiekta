

'''
SITE ID information

https://public-api.wordpress.com/rest/v1/sites/greenskymedia.wordpress.com/?pretty=1

{
    "ID": 56993732,
    "name": "Information and Media at GreenSky - KrishiEkta Information and Knowledge Distribution System",
    "description": "GreenSky India&#039;s KrishiEkta brings together knowledge and information on Agriculture in India.",
    "URL": "http:\/\/greenskymedia.wordpress.com",
    "meta": {
        "links": {
            "self": "https:\/\/public-api.wordpress.com\/rest\/v1\/sites\/56993732",
            "help": "https:\/\/public-api.wordpress.com\/rest\/v1\/sites\/56993732\/help",
            "posts": "https:\/\/public-api.wordpress.com\/rest\/v1\/sites\/56993732\/posts\/",
            "comments": "https:\/\/public-api.wordpress.com\/rest\/v1\/sites\/56993732\/comments\/"
        }
    }
}
'''


import urllib.request
import urllib.parse
import json

url = 'https://public-api.wordpress.com/rest/v1/sites/56993732/posts/new/'

headers = {	'authorization':"bearer N5Eq4T^a%Q#Oijm1ARY9Rf2fTVxUJaJfpat%0l#7dWFH1t3pkZzxg8ebWNvleu(j",
		'Content-Type':'application/x-www-form-urlencoded',
	  }

values ={	'title' : 'Testing Post from KrishiEkta - #1',
		'content' : 'This is a test post sent from the KrishiEkta system.',
		'publicize' : False,
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
