# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2018 Digi International Inc. All Rights Reserved.

# Takes input from Serial Port 0 and publishes it over MQTT to an MQTT broker
# Connect over serial with Putty or similar utility for testing

import paho.mqtt.client as mqtt
import ssl
import select

# remember to respect 8.3 file format
ver = "ver.crt" # path to root CA
prv = "prv.key" # path to private key
crt = "crt.crt" # path to cert

client_name = "example"
username = "example"
password = None

connect_url = "example-url"
port = 8883 # 1883 if not SSL/TLS
timeout = 600

topic = "serial"
qos = 0

# define function to run whenever a message is published
def on_publish(client, userdata, mid):
	print("publish successful")

	# after publishing disconnect, breaks out of loop_forever()
	client.disconnect()
	pass


# name your client whatever you want
client = mqtt.Client(client_name)

# set your username/password
client.username_pw_set(username=username, password=password)

# not needed if not doing SSL/TLS
client.tls_set( ca_certs=ver, certfile=crt, keyfile=prv,
	cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_SSLv23)

# assign function to be run whenever a message is published
client.on_publish = on_publish

print("connecting...")

# connect to your desired url:port with specified timeout
check = client.connect(connect_url, port, timeout)

if(check == mqtt.MQTT_ERR_SUCCESS):
	print("connection succeded")
else:
	print("connect failed")
	exit(1)

# open the serial port
fd = open('ASY/00', 'r')

# start the client, non blocking
client.loop_start()

# publish 5 messages and exit
for i in range(5):
	print("Type input: ")
	input = get_serial()

	client.publish(topic, input, qos)


# stop the client
client.loop_stop()

print("disconnecting...")
client.disconnect()

exit(0)
