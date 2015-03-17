#!/usr/local/bin/python3

from datetime import datetime
from datetime import date
from datetime import time

today = date.today()
form1 = today.strftime("%m/%d/%y")
form2 = today.strftime("%a, %d %b %Y")

print (today)
print (form1)


abstime = datetime.now()

time2 = datetime(2013,10,20,12,12,12)

form5 = time2.strftime("%a, %d %b %Y %H:%M:%S +0530")

form3 = str(abstime) #.isoformat #strftime("") #"%a, %d %b %Y %H:%M:%S ")

form4 = abstime.strftime("%A %b %d %H:%M:%S EST %Y")


comp_time1 = datetime.strptime(form5,"%a, %d %b %Y %H:%M:%S +0530")
comp_time2 = datetime.strptime(form4,"%A %b %d %H:%M:%S EST %Y")

print(comp_time1)
print(comp_time2)


if(comp_time1<comp_time2):
	print("Abstime comes late")

print (abstime)
print (time2)
print ("Form2: ", form2)
print ("Form3: ", form3)
print ("Form4: ", form4)
