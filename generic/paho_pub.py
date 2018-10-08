# Publishes a predefined message over MQTT to an MQTT broker

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

topic = "example/test"
payload = "Hello from paho_pub!"
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

print("publishing...")
client.publish(topic, payload, qos)

# start the client, blocks
client.loop_forever()

exit(0)
