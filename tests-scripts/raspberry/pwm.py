#!/usr/bin/python

import RPi.GPIO as GPIO
from optparse import OptionParser
import time

if __name__ == "__main__":
	parser = OptionParser(usage="usage: %prog [options]")
	parser.add_option("-p", "--pin",
			  type="int",
			  dest="pin",
			  help="PWM pin on Raspberry Pi3 board, 12 by default",
			  default=12)
	parser.add_option("-f", "--frequency",
			  type="int",
			  dest="frequency",
			  help="PWM frequency, 50Hz by default",
			  default=50)
	parser.add_option("-d", "--duty_cycle",
			  type="int",
			  dest="dutyCycle",
			  help="PWM duty cycle, 50% by default",
			  default=50)
	parser.add_option("-t", "--duration",
			  type="int",
			  dest="duration",
			  help="PWm duration, 1s by default",
			  default=1)
	(options, args) = parser.parse_args()

	# Init GPIO
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(options.pin,GPIO.OUT)

	# Configure ad start PWM
	my_pwm=GPIO.PWM(options.pin,options.frequency)
	my_pwm.start(float(options.dutyCycle))

	time.sleep(options.duration)

	# Stop PWM
	my_pwm.stop()

	# Clean GPIO
	GPIO.cleanup()

