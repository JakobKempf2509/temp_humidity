#!/usr/bin/env python

#Dieses Programm dient zum lesen der Temperatur und Luftfeuchtigkeit (This program is used to measure temperature and humidity)
#J. Kempf 2020-04-24

#import library
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

#conditions
abbruch = True

#set variable
my_sensor = Adafruit_DHT.DHT11

#set the GPIO the sensor is connected to 
GPIO.setmode(GPIO.BCM)
my_gpio = 4 

while abbruch:
    try:
        #read the humidity and temperature
        my_humidity, my_temperature = Adafruit_DHT.read(my_sensor, my_gpio)

        #control of reading
        if my_humidity is not None and my_temperature is not None:
            print('The current temperature is: {0:0.1f} °C , The current humidity is: {1:0.1f} %'.format(my_temperature , my_humidity))
            abbruch = False
        else: 
            print("The reading process is failed, please try it again.")
            abbruch = True
    except ValueError:
        print("Error, try it again...")

GPIO.cleanup()