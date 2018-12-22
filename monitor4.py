#Crusher 4

import time
import smbus
import mcp3428
import Adafruit_BBIO.GPIO as GPIO
import os

GPIO.setup("P8_12", GPIO.IN)
#GPIO.add_event_detect("P8_12", GPIO.RISING)
# Get I2C bus, this is I2C Bus 2
bus = smbus.SMBus(2)

#kwargs is a Python set that contains the address of your device as well as additional device and calibration values.
#kwargs does not have to be populated as every value is optional and will be replaced with a default value if not is specified.

#below is an example of a kwarg declaration that is populated with all of the default values for each user configurable property
#refer to the datasheet for this chip to calculate what values you should be using for your project.
kwargs = {'address': 0x6E, 'mode': 0x10, 'sample_rate': 0x08, 'gain': 0x01}

#create the MCP3428 object from the MCP3428 library
#the object requires that you pass it the bus object so that it can communicate and share the bus with other chips if necessary
mcp3428 = mcp3428.MCP3428(bus, kwargs)

while True :
	if GPIO.input("P8_12") == True:
	#if GPIO.event_detected("P8_12") == True:
		time.sleep(0.1)
		if GPIO.input("P8_12") == True:
			print "Crusher ON"
			time.sleep(5)
			flow = mcp3428.take_single_reading(2)
			print flow
	else:
		print "Crusher OFF"