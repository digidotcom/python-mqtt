# Takes input from Serial Port 0 and publishes it over MQTT to AWS IoT
# Connect over serial with Putty or similar utility

import paho.mqtt.client as mqtt
import ssl
import select

# open the serial port
fd = open('ASY/00', 'r')

# remember to respect 8.3 file format
ver = "ver_pem.crt" # path to root CA
prv = "prv_pem.key" # path to private key
crt = "crt_pem.crt" # path to cert


# define function to get input from serial port
def get_serial():
	global fd
	string = ""
	ch = ""

	# read input a character at a time until a LF is received
	while ch != "\n":
		# wait 10 secs for input data on fd
		waitreadresult = select.select([fd], [], [], 10)

		if not fd in waitreadresult[0]:
			print("\r\nNo input received from serial port\r\n")
			break

		ch = fd.read(1)

		if ch != "\n":
			string += ch

	return string


# define function to run whenever a message is published
def on_publish(client, userdata, mid):
	print("publish success")
	pass


# name your client whatever you want
client = mqtt.Client("abc123")

# client username must be "?SDK=Python&Version=1.4.0" to work with AWS IoT
client.username_pw_set("?SDK=Python&Version=1.4.0")

client.tls_set( ca_certs=ver, certfile=crt, keyfile=prv,
	cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_SSLv23)

# assign funtion to be run whenever a message is published
client.on_publish = on_publish

print("connecting...")

# connect to your desired AWS URL, on port 883 (encrypted MQTT), with a largeish timeout
check = client.connect("your-url.amazonaws.com", 8883, 600)

if(check == mqtt.MQTT_ERR_SUCCESS):
	print("connection succeded")
else:
	print("connect failed")
	exit(1)


# start the client, non blocking
client.loop_start()

topic = "serial"

# publish 10 messages and exit
for i in range(10):
	print("Type input: ")
	input = get_serial()

	client.publish(topic, input)



# stop the client
client.loop_stop()

print("disconnecting...")
client.disconnect()

exit(0)
