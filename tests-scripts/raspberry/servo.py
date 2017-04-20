#!/usr/bin/python

import RPi.GPIO as GPIO
from optparse import OptionParser
import time
#import sys

if __name__ == "__main__":
	parser = OptionParser(usage="usage: %prog [options]")
	parser.add_option("-p", "--pin",
			  type="int",
			  dest="pin",
			  help="PWM pin on Raspberry Pi3 board, 12 by default",
			  default=12)
	parser.add_option("-a", "--angle",
			  type="int",
			  action='append',
			  dest="angles",
			  help="Servo angle(s)")
	parser.add_option("-i", "--interval",
			  type="int",
			  dest="interval",
			  help="Time interval between angles, default 0",
			  default=1)
	parser.add_option("-o", "--occurence",
			  type="int",
			  dest="occurence",
			  help="Number of time to repeat the list of angles, default 1",
			  default=1)
	(options, args) = parser.parse_args()

	# Init GPIO
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(options.pin,GPIO.OUT)

	# Configure ad start PWM
	my_pwm=GPIO.PWM(options.pin, 50)
	my_pwm.start(float(0))

	loops = options.occurence
	while loops:
		for angle in options.angles:
			# TODO: Compute duty cycle from the angle
			my_pwm.ChangeDutyCycle(angle)
			time.sleep(options.interval)

		loops-= 1

	# Stop PWM
	my_pwm.stop()

	# Clean GPIO
	GPIO.cleanup()

