# Py-SIM800L-SMS :radio: :computer: :phone: :incoming_envelope:

## Summary
#### What is SMS?
SMS (short message service) is a text messaging service component of most telephone, Internet, and mobile device systems. It uses standardized communication protocols to enable mobile devices to exchange short text messages. An intermediary service can facilitate a text-to-voice conversion to be sent to landlines. SMS was the most widely used data application at the end of 2010, with an estimated **3.5 billion** active users, or about 80% of all mobile subscribers.

SMS, as used on modern devices, originated from radio telegraphy in radio memo pagers that used standardized phone protocols. These were defined in **1985** as part of the Global System for Mobile Communications (GSM) series of standards. The first SMS message was sent in **1992**.

The protocols allowed users to send and receive messages of up to **160 characters** (when entirely alpha-numeric) to and from GSM mobiles. Although most SMS messages are mobile-to-mobile text messages, support for the service has expanded to include other mobile technologies, such as ANSI CDMA networks and Digital AMPS.

## Requirements
- ``Python 2.7 or Python 3.4 and newer``

- ``If running on Windows: Windows 7 or newer``

## Installation

This installs a package that can be used from Python:

```python
   import serial
```
### From PyPI

pySerial can be installed from PyPI:

    python -m pip install pyserial

Using the `python`/`python3` executable of the desired version (2.7/3.x). 

Developers also may be interested to get the source archive, because it
contains examples, tests and the this documentation. By using PyPI, you will be using the latest stable version.

--------------------

## Pinout
![alt iviny](https://github.com/MortadhaDAHMANI/Py-SIM800L/raw/master/original.jpg)

```diff
- NOTICE: Be prepared to handle huge power consumption with peek up to 2A. Maximum voltage on UART in this module is 2.8V. Higher voltage will kill the module.
```

### Useful links
* [AT Commands](https://nettigo.eu/attachments/386 "AT Commands")
* [Hardware Design](https://nettigo.eu/attachments/385 "Hardware Design")
* [Specification](https://nettigo.eu/products/sim800l-gsm-grps-module "Specification")
* [Tutorial Arduino](https://lastminuteengineers.com/sim800l-gsm-module-arduino-tutorial/ "Arduino")
* [Arduino Library](https://github.com/cristiansteib/Sim800l "Arduino Lib.")
* [PySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html "PySerial")
* [PySerial Git](https://github.com/pyserial/pyserial "PySerial Git")

### Donation
If this project help you, you can give me a tip ;)

<a href="https://paypal.me/mamdpay" rel="In"> <img src="https://www.pngarts.com/files/4/Paypal-Donate-PNG-High-Quality-Image.png" alt="Donation" height="70"></a>

### Author
* This version has been created by: [**Mortadha DAHMANI**](mailto:mortadha.dahmani@gmail.com)

<a href="https://www.linkedin.com/in/mortadhadahmani" rel="In"> <img src="https://github.com/MortadhaDAHMANI/Py-SIM800L/raw/master/in2.jpg" alt="In" height="40"></a>

### Revision History
* Initial Release : 20 June 2017

### License
* Py-SIM800L-SMS is distributed under the **LGPL** version 3 license.
