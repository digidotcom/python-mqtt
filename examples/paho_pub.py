# Publishes a predefined message over MQTT to AWS IoT and exits

import paho.mqtt.client as mqtt
import ssl

# remember to respect 8.3 file format
ver = "ver_pem.crt" # path to root CA
prv = "prv_pem.key" # path to private key
crt = "crt_pem.crt" # path to cert


# define function to run whenever a message is published
def on_publish(client, userdata, mid):
	print("publish successful")

	# after publishing disconnect
	client.disconnect()
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

if(check == mqtt.MQTT_ERR_SUCCESS):
	print("connection succeded")
else:
	print("connect failed")
	exit(1)

topic = "saros/test"
payload = "Hello from SarOS"

print("publishing...")
client.publish(topic, payload)

# start the client, blocks
client.loop_forever()

exit(0)
