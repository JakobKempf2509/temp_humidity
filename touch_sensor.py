#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.input(17)

while True:
    if GPIO.input(17) == 1:
        print("Taster nicht gedrückt")
    else:
        print("Taster gedrückt gedrückt")



