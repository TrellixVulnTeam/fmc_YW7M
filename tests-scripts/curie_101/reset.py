#!/usr/bin/python

# Reset the Curie 101 board.
# Reset button is connected to the USB-RLY08 relay 1
# We suppose the USB-RLY08 is enumerated as /dev/ttyUSB0

import serial
import time

if __name__ == "__main__":
	ser = serial.Serial(
	    port='/dev/ttyUSB0',
	    baudrate=19200,
	    parity=serial.PARITY_NONE,
	    stopbits=serial.STOPBITS_TWO,
	    bytesize=serial.EIGHTBITS,
	    xonxoff=serial.XOFF,
	    rtscts=False,
	    dsrdtr=False
	)

	# USB-RLY08 board commands
	# d: All relays ON
	# e: Relay 1 ON
	# f: Relay 2 ON
	# g: Relay 3 ON
	# h: Relay 4 ON
	# i: Relay 5 ON
	# j: Relay 6 ON
	# k: Relay 7 ON
	# l: Relay 8 ON

	# n: All relays OFF
	# o: Relay 1 OFF
	# p: Relay 2 OFF
	# q: Relay 3 OFF
	# r: Relay 4 OFF
	# s: Relay 5 OFF
	# t: Relay 6 OFF
	# u: Relay 7 OFF
	# v: Relay 8 OFF


	# Reset the board
	ser.write('e')

	# Wait for 1 second
	time.sleep(1)

	# Release the reset button
	ser.write('o')

	ser.close()

