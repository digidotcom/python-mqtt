# Subcribes to a topic and receives messages over MQTT from AWS IoT

import paho.mqtt.client as mqtt
import ssl

# remember to respect 8.3 file format
ver = "ver_pem.crt" # path to root CA
prv = "prv_pem.key" # path to private key
crt = "crt_pem.crt" # path to cert


subscription = "test/#"

# define function to run whenever a connection is made
def on_connect(client, userdata, flags, rc):
	global subscription

	print("Connected with return code: " +str(rc))

	client.subscribe(subscription, 1)

	print("Subscribed to: " +subscription)


message_counter = 0

# define function to run whenever a message is received
def on_message(client, userdata, message):
	global message_counter
	message_counter += 1

	print("Got payload:")
	print(message.payload)
	print("From topic:")
	print(message.topic)
	print("")

	if message_counter >= 3:
		client.disconnect()


# name your client whatever you want
client = mqtt.Client("abc123")

# client username must be "?SDK=Python&Version=1.4.0" to work with AWS IoT
client.username_pw_set("?SDK=Python&Version=1.4.0")

client.tls_set( ca_certs=ver, certfile=crt, keyfile=prv,
	cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_SSLv23)

# assign function to run whenever a connection is made/message is published
client.on_connect = on_connect
client.on_message = on_message

print("connecting...")

# connect to your desired AWS URL, on port 883 (encrypted MQTT), with a largeish timeout
check = client.connect("your-url.amazonaws.com", 8883, 600)

if(check == mqtt.MQTT_ERR_SUCCESS):
	print("connection succeded")
else:
	print("connect failed")

# start the client, blocking
print("looping forever")
client.loop_forever()

exit(0)
