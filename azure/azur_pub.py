# Publishes a predefined message over MQTT to MS Azure IoT Hub and exits

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

topic = "devices/" + device_id + "/messages/events/"
payload = "Hello Azure!"
qos = 1

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
