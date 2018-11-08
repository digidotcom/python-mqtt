# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2018 Digi International Inc. All Rights Reserved.

# Takes input from a keyboard and publishes it over MQTT to AWS IoT

import paho.mqtt.client as mqtt
import ssl
import wr31_dio # get from wr31_io_lib
from time import sleep

# remember to respect 8.3 file format
ver = "ver_pem.crt" # path to root CA
prv = "prv_pem.key" # path to private key
crt = "crt_pem.crt" # path to cert

client_name = "example"
username = "example"
password = None

connect_url = "example-url"
port = 8883 # 1883 if not SSL/TLS
timeout = 600

topic_0 = "wr31/dio/0/state"
topic_1 = "wr31/dio/1/state"
payload = "Hello from paho_pub!"
qos = 0

# define function to run whenever a message is published
def on_publish(client, userdata, mid):
	print("publish successful")
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

if check == mqtt.MQTT_ERR_SUCCESS:
	print("connection succeded")
else:
	print("connect failed")
	exit(1)


# start the client, non blocking
client.loop_start()

# publish 5 messages and exit
for i in range(5):
	dio_0_state = "On" if wr31_dio.dio_read(0) else "Off"
	dio_1_state = "On" if wr31_dio.dio_read(1) else "Off"

	client.publish(topic_0, dio_0_state)
	client.publish(topic_1, dio_1_state)

	sleep(4)


# stop the cient
client.loop_stop()

print("disconnecting...")
client.disconnect()

exit(0)
