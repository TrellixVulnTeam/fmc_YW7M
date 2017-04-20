#!/usr/bin/python

import RPi.GPIO as GPIO
from optparse import OptionParser
import time

if __name__ == "__main__":
	parser = OptionParser(usage="usage: %prog [options]")
	parser.add_option("-p", "--pin",
			  type="int",
			  dest="pin",
			  help="PWM pin on Raspberry Pi3 board, 7 by default",
			  default=7)
	(options, args) = parser.parse_args()

	# Init GPIO
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(options.pin,GPIO.OUT)

	GPIO.output(options.pin, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(options.pin, GPIO.LOW)

	# Clean GPIO
	GPIO.cleanup()

