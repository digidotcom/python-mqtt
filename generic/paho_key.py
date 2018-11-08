# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2018 Digi International Inc. All Rights Reserved.

# Takes input from a keyboard and publishes it over MQTT an MQTT broker

import paho.mqtt.client as mqtt
import ssl

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

# start the client, non blocking
client.loop_start()

# get input from keyboard
topic = raw_input("Enter topic: ")

# publish 5 messages and exit
for i in range(5):
	message = raw_input("\nEnter message " + str(i) + " to publish:")
	client.publish(topic, message, qos)


# stop the cient
client.loop_stop()

print("disconnecting...")
client.disconnect()

exit(0)
