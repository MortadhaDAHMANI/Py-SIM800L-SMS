#!/usr/bin/python3
# -*- coding: utf8 -*-

import time
import serial

recipient = "+33751277743"
message = "Hello, World!"

phone = serial.Serial("/dev/ttyUSB0",  115200, timeout=2)
try:
    time.sleep(0.5)
    phone.write(b'AT\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGF=1\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
    time.sleep(0.5)
    phone.write(message.encode() + b"\r")
    time.sleep(0.5)
    phone.write(bytes([26]))
    time.sleep(0.5)
finally:
    phone.close()
