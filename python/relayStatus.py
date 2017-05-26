#!/usr/bin/env python
import RPi.GPIO as GPIO

def getStatus():

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	pin = 18

	GPIO.setup(pin, GPIO.OUT)

	if(GPIO.input(pin) == 1):
		print("ON")
		return "ON"
	else:
		print("OFF")
		return "OFF"
		
if(__name__ == "__main__"):
	getStatus()


