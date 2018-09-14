# Takes input from a keyboard and publishes it over MQTT to AWS IoT

import paho.mqtt.client as mqtt
import ssl

# remember to respect 8.3 file format
ver = "ver_pem.crt" # path to root CA
prv = "prv_pem.key" # path to private key
crt = "crt_pem.crt" # path to cert


# define function to run whenever a message is published
def on_publish(client, userdata, mid):
	print("publish successful")
	pass


# name your client whatever you want
client = mqtt.Client("abc123")

# client username must be "?SDK=Python&Version=1.4.0" to work with AWS IoT
client.username_pw_set("?SDK=Python&Version=1.4.0")


client.tls_set( ca_certs=ver, certfile=crt, keyfile=prv,
	cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_SSLv23)

# assign function to be run whenever a message is published
client.on_publish = on_publish

print("connecting...")

# connect to your desired AWS URL, on port 883 (encrypted MQTT), with a largeish timeout
check = client.connect("your-url.amazonaws.com", 8883, 600)

if check == mqtt.MQTT_ERR_SUCCESS:
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
	client.publish(topic, message)


# stop the cient
client.loop_stop()

print("disconnecting...")
client.disconnect()

exit(0)
