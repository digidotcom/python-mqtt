# AWS MQTT using Python on WR21, WR31, WR44
-------------------------------------------


### Helpful References
- [AWS IoT Getting Started](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html)
- [AWS X.509 Certificates](https://docs.aws.amazon.com/iot/latest/developerguide/managing-device-certs.html)
- [MQTT](http://mqtt.org/)
- [Paho Python](https://github.com/eclipse/paho.mqtt.python)


### Paho
__The Paho library in this directory has been modified__. The standard Paho library does not run on the Python implementation that ships with these devices. The standard Paho library as well as its documentation can be found [here](https://github.com/eclipse/paho.mqtt.python).

This Python implementation does not include support for non blocking sockets which are relied on by Paho for threading. So Paho's thread support has been removed.

This Python implementation has an older version of Python's SSL library that does not include _SSLContext_. `ssl.wrap_socket()` is called directly instead. However, the _cipher_ argument for `ssl.wrap_socket()` is not included.

This Python implementation's SSL library does not have `ssl.match_hostname`, so Paho's `client.tls_set_insecure` method has been removed.

This modified Paho library has not been extensively tested.


### Run on a Device
To run these files on a device edit them with your AWS IoT creds and certs. The flat file system and 8.3 file format of the target devices adds some inconvenience. The Paho library needs to be zipped. If the zip file is not present, create it by zipping the paho folder. Create *prv_pem.crt* and *cert_pem.crt* with your respective private key and cert, and *ver_pem.crt* with your root CA.
Then move your:
- zipped paho archive
- cert it pem format
- private key in pem format
- verifier in pem format
- example/target python file

onto the device. Add paho.zip to the devices Python path, and run the target Python file with `python file.py`.

Alternatively the examples can be run locally if you correct the file paths.


-----------
### License


This software is open-source. Copyright (c), Digi International Inc., 2018.

This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file, you can obtain one at
http://mozilla.org/MPL/2.0/.

The Paho library code is subject to the terms of the Eclipse Public License 1.0 and the Eclipse Distribution License 1.0. These can be found under the paho/ directory.
If they are not found there, they can be obtained at http://www.eclipse.org/org/documents/epl-1.0/EPL-1.0.txt and https://www.eclipse.org/org/documents/edl-v10.html.

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
