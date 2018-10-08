# AWS MQTT using Python on WR21, WR31, WR44
-------------------------------------------


### Helpful References
- [AWS IoT Getting Started](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html)
- [AWS IoT X.509 Certificates](https://docs.aws.amazon.com/iot/latest/developerguide/managing-device-certs.html)
- [Azure IoT Hub Getting Started](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support)
- [Azure IoT Security](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-security)
- [MQTT](http://mqtt.org/)
- [Paho Python](https://github.com/eclipse/paho.mqtt.python)


### The Examples
In __generic__ are 4 Paho MQTT examples that can be easily modified to work with a generic MQTT broker. _paho_pub.py_ and _paho_sub.py_ are straight forward examples of publishing and subscribing with Paho MQTT. _paho_key_ publishes input taken from the keyboard, and _paho_ser.py_ publishes input taken from the serial port.

In __aws__ are skeletons for talking MQTT to AWS IoT. They are straightforward examples and should be easily adapted for your needs. To talk to AWS IoT over MQTT you first need to get your device configured in the AWS IoT Core and set up certs. See links above for how to do this.

In __azure__ are skeletons for talking to Azure IoT Hub. They are straightforward examples and should be easily adapted for your needs. These skeletons are set up to talk to Azure IoT Hub using x509 certificates and will need to be modified if you wish to use SAS tokens. To talk to Azure IoT over MQTT you first need to get your device configured in the Azure IoT Hub and set up certs. See links above for how to do this.


-------------------
### Run on a Device
After editing the files to work with your MQTT broker put, your target Python file, any needed cert or key files, and _paho.zip_ onto the device. (_paho.zip_ is simply a _paho/_ zipped) Remember to respect the device's 8.3 file format and flat file system. Add _paho.zip_ to the device's Python path and run your target file with `python file.py`.

The target file can also be run locally with Python2.


--------
### Paho
__The Paho library in this directory has been modified__. The standard Paho library does not run on the Python implementation that ships with these devices. The standard Paho library as well as its documentation can be found [here](https://github.com/eclipse/paho.mqtt.python).

This Python implementation does not include support for non blocking sockets which are relied on by Paho for threading. So Paho's thread support has been removed.

This Python implementation has an older version of Python's SSL library that does not include _SSLContext_. `ssl.wrap_socket()` is called directly instead. However, the _cipher_ argument for `ssl.wrap_socket()` is not included.

This Python implementation's SSL library does not have `ssl.match_hostname`, so Paho's `client.tls_set_insecure` method has been removed.

This modified Paho library has not been extensively tested.


-----------
### License


This software is open-source. Copyright (c), Digi International Inc., 2018.

This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file, you can obtain one at
http://mozilla.org/MPL/2.0/.

The Paho library code is subject to the terms of the Eclipse Public License 1.0 and the Eclipse Distribution License 1.0. These can be found under the paho/ directory.
If they are not found there, they can be obtained at http://www.eclipse.org/org/documents/epl-1.0/EPL-1.0.txt and https://www.eclipse.org/org/documents/edl-v10.html respectively.

Digi, Digi International, the Digi logo, the Digi website, and Digi
Device Cloud are trademarks or registered trademarks of Digi
International, Inc. in the United States and other countries
worldwide. All other trademarks are the property of their respective
owners.

THE SOFTWARE AND RELATED TECHNICAL INFORMATION IS PROVIDED "AS IS"
WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL DIGI OR ITS
SUBSIDIARIES BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
OF OR IN CONNECTION WITH THE SOFTWARE AND TECHNICAL INFORMATION
HEREIN, INCLUDING ALL SOURCE AND OBJECT CODES, IRRESPECTIVE OF HOW IT
IS USED. YOU AGREE THAT YOU ARE NOT PROHIBITED FROM RECEIVING THIS
SOFTWARE AND TECHNICAL INFORMATION UNDER UNITED STATES AND OTHER
APPLICABLE COUNTRY EXPORT CONTROL LAWS AND REGULATIONS AND THAT YOU
WILL COMPLY WITH ALL APPLICABLE UNITED STATES AND OTHER COUNTRY EXPORT
LAWS AND REGULATIONS WITH REGARD TO USE AND EXPORT OR RE-EXPORT OF THE
SOFTWARE AND TECHNICAL INFORMATION.
