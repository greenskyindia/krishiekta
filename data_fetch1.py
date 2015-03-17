#!/usr/local/bin/python3

import subprocess
import urllib.request
import json
import datetime
import sys

url = 'http://www.thehindubusinessline.com/opinion/columns/g-chandrashekhar/ctt-on-essential-food-items-unwarranted/article4840830.ece'

f = urllib.request.urlopen(url) 

file1 = open('data001/file1.html','w')

file1.write(str(f.read())) 

f.close()
file1.close()
