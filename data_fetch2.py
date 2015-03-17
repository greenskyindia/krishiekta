#!/usr/local/bin/python3

import subprocess
import urllib.request
import json
import datetime
import sys

#url = 'http://www.thehindubusinessline.com/industry-and-economy/agri-biz/pepper-gains-on-supply-squeeze/article5029462.ece'
url = 'http://economictimes.indiatimes.com/news/economy/agriculture/cotton-farmers-in-haryana-advised-to-monitor-crop-against-pests/articleshow/22100493.cms'

local_file = 'data001/file4download.html'

#f = urllib.request.urlopen(url) 

urllib.request.urlretrieve(url, local_file)

#print headers

