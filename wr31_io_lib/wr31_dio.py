# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2018 Digi International Inc. All Rights Reserved.

import sarcli

# library summary for users:
#	pin_summary(pin_num):
#		prints everything there is to know about the given pin

#	dio_read(pin_num):
#		reads given pin and returns True if DIN=HIGH or False if DIN=LOW

#	dio_check(pin_num):
#		checks the state of the given PIN, returns True if DOUT=ON or False if DOUT=OFF

#	dio_set(pin_num, state):
#		sets DOUT for the given pin to the given state, either ON or OFF

#	dio_pullup_check(pin_num):
#		checks the pullup state of the given pin, returns True if Pullup=ON or False if Pullup=OFF

#	dio_pullup_set(pin_num, state):
#		sets Pullup for the given pin to the given state, either ON or OFF

def pin_summary(pin_num):
	"""
	print a summary of the given digital pin

	pin_num: 0 or 1

	returns: nothing
	"""

	if not validate_pin_num(pin_num):
		print("Error: must select pin 0 or 1")
		return

	print "PIN 0"
	print "DOUT   : " + str("ON" if dio_check(pin_num) else "OFF")
	print "DIN    : " + str("HIGH" if dio_read(pin_num) else "LOW")
	print "Pullup : " + str("ON" if diopullup_check(pin_num) else "OFF")

	return


def dio_read(pin_num):
	"""Read digital io pin 0 or 1 (DIN=?)

	pin_num: 0 or 1

	returns: true if given pin reads HIGH (DIN=HIGH)
	         false if given pin reads LOW (DIN=LOW)
	         nothing if error
	"""

	if not validate_pin_num(pin_num):
		print("Error: must select pin 0 or 1")
		return

	gpio_dio = cli_command("gpio dio")

	lines = gpio_dio.splitlines()
	line_words = lines[pin_num].split()
	high_low = line_words[2][4:]

	if high_low == "HIGH":
		return True
	elif high_low == "LOW":
		return False
	else:
		return


def dio_check(pin_num):
	"""Check state of digital io pin 0 or 1 (DOUT=?)

	pin_num: 0 or 1

	returns: true if DOUT=ON
	         false if DOUT=OFF
	         nothing if error
	"""
	if not validate_pin_num(pin_num):
		print("Error: must select pin 0 or 1")
		return

	gpio_dio = cli_command("gpio dio")

	lines = gpio_dio.splitlines()
	line_words = lines[pin_num].split()
	on_off = line_words[1][5:]

	if on_off == "ON":
		return True
	elif on_off == "OFF":
		return False
	else:
		return


def dio_set(pin_num, state):
	"""Set the state of digital io pin 0 or 1 (DOUT=?)

	pin_num: 0 or 1

	returns: nothing
	"""

	if not validate_pin_num(pin_num):
		print("Error: must select pin 0 or 1")
		return

	state = state.lower()

	if not validate_pin_state(state):
		print("Error: state must be on or off")
		return

	cmd = "gpio dio -D" + str(pin_num) + " " + state

	cli_command(cmd)
	return


def diopullup_check(pin_num):
	"""Check that pullup status of digital io pin 0 or 1

	pin_num: 0 or 1

	returns: true if pullup is on
	         false if pullup is off
	         nothing on error
	"""

	if not validate_pin_num(pin_num):
		print("Error: must select pin 0 or 1")
		return

	gpio_diopullup = cli_command("gpio diopullup")

	lines = gpio_diopullup.splitlines()
	line_words = lines[pin_num].split()
	on_off = line_words[1][7:]

	if on_off == "ON":
		return True
	elif on_off == "OFF":
		return False
	else:
		return


def diopullup_set(pin_num, state):
	"""Set the pullup state of digital io pin 0 or 1

	pin_num: 0 or 1
	state: on or off

	returns: nothing
	"""

	if not validate_pin_num(pin_num):
		print("Error: must select pin 0 or 1")
		return

	state = state.lower()

	if not validate_pin_state(state):
		print("Error: state must be on or off")
		return

	cmd = "gpio diopullup -D" + str(pin_num) + " " + state

	cli_command(cmd)
	return


	####################
	# Helper Functions #
	####################

def cli_command(cmd):
	"""Send a command to the cli, get output

	cmd: a string that is the cli command to be issued

	returns: a stripped string that is the output of the cli command
	"""

	data = ""

	cli = sarcli.open()
	cli.write(cmd)
	while True:
		tmpdata = cli.read(-1)
		if not tmpdata:
			break
		data += tmpdata
	cli.close()

	return data.strip()


def validate_pin_num(pin_num):
	"""Validates that the given number corresponds to a pin

	pin_num: an int

	returns true if pin_num is 0 or 1
	"""
	return pin_num == 0 or pin_num == 1


def validate_pin_state(state):
	"""Validates the given state

	state: a string

	returns: true if state is "on" or "off"
	"""
	return state == "on" or state == "off"
