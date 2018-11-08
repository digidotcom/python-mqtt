# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2018 Digi International Inc. All Rights Reserved.

# Subcribes to a topic and receives 3 messages over MQTT from an MQTT broker

import paho.mqtt.client as mqtt
import ssl

# remember to respect 8.3 file format
# make sure SHA1 fingerprint of crt is added to device
ver = "azur_ver.crt" # path to root CA
prv = "prv.key" # path to private key
crt = "crt.crt" # path to cert

device_id = "your-device-id"
iot_hub_name = "your-iot-hub-name"

client_name = device_id
username = iot_hub_name + ".azure-devices.net/" + device_id
password = None

connect_url = iot_hub_name + ".azure-devices.net"
port = 8883
timeout = 600

subscription = "devices/" + device_id + "/messages/devicebound/#"
qos = 1

print("connect_url: " + connect_url)

# define function to run whenever a connection is made
def on_connect(client, userdata, flags, rc):
	global subscription

	print("Connected with return code: " +str(rc))

	client.subscribe(subscription, qos)

	print("Subscribed to: " +subscription)


message_counter = 0
max_message = 3

# define function to run whenever a message is received
def on_message(client, userdata, message):
	global max_message
	global message_counter
	message_counter += 1

	print("Got payload:")
	print(message.payload)
	print("From topic:")
	print(message.topic)
	print("")

	if message_counter >= max_message:
		client.disconnect()


# name your client whatever you want
client = mqtt.Client(client_name)

# set your username/password
client.username_pw_set(username=username, password=password)

client.tls_set( ca_certs=ver, certfile=crt, keyfile=prv,
	cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_SSLv23)

# assign function to run whenever a connection is made/message is published
client.on_connect = on_connect
client.on_message = on_message

print("connecting...")

# connect to your desired url:port with specified timeout
check = client.connect(connect_url, port, timeout)

if(check == mqtt.MQTT_ERR_SUCCESS):
	print("connection succeded")
else:
	print("connect failed")

# start the client, blocking
print("looping forever")
client.loop_forever()

exit(0)
