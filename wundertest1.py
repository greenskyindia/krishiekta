#!/usr/local/bin/python 

import subprocess
import urllib, urllib2, json
import datetime
import MySQLdb,sys

url= 'http://api.wunderground.com/api/caea5fe4b5fa4940/conditions/q/-33.389,150.234.json'

f = urllib2.urlopen(url) 

json_string = f.read() 

parsed_json = json.loads(json_string) 

location = parsed_json['current_observation']['display_location']['city'] 

temp_c = parsed_json['current_observation']['temp_c'] 

wind = parsed_json['current_observation']['wind_kph']

print "Current temperature in %s is: %s" % (location, temp_c) 
print "Wind speed is: %s Kph" % (wind)

f.close()
