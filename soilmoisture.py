#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)

time.sleep(1)

while True:
    time.sleep(1)
    if (GPIO.input(15)):
        print ("no water detected!")
    else:
        print ("Water detected!")
