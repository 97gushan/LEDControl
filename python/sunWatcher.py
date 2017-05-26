#!/usr/bin/pythonz
import requests

def getFormatedTime(unformated_time):
	length = len(unformated_time)

	for n in range(0, length):
		if(unformated_time[n] == "T"):
			return unformated_time[n+1] + unformated_time[n+2]
	
r = requests.get("https://api.sunrise-sunset.org/json?lat=65.584819&lng=22.1567026&date=today&formatted=0"
)

sunrise =   r.json()['results']['sunrise']
sunset =   r.json()['results']['sunset']

time_sunrise = getFormatedTime(sunrise)
time_sunset = getFormatedTime(sunset)

print(sunrise)
print(sunset)

print(time_sunrise)
print(time_sunset)

f = open("sun.txt", 'w')
f.write(time_sunrise + "\n"+time_sunset)
f.close()
	
	
	
	
