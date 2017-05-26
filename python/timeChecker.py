#!/usr/bin/python

import datetime
import relayScript

f = open("/home/pi/sun.txt")

time_sunrise = int(f.readline()) +1 +1	# +1 to compensate for UTC+1
time_sunset = int(f.readline()) +1 +1  	# +1 to compensate for summer time

f.close()

time_now = datetime.datetime.now().hour        
time_now = time_now % 24
	
print(time_now)
print(time_sunrise)
print(time_sunset)
	
if(time_now == time_sunrise):
	relayScript.turnOff()
	
if(time_now == time_sunset):
	relayScript.turnOn()
