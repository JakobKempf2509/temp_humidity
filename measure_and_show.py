#!/usr/bin/env python

#This programcode measure the temperature and the humidity and show it on a lcd-display
#J. Kempf 2020-04-27

#import library
import RPi.GPIO as GPIO
import Adafruit_DHT
from time import*
import time
import lcddriver

#conditions
abbruch = True
start = True

#set variables
my_sensor = Adafruit_DHT.DHT11
my_lcd = lcddriver.lcd()

my_lcd.lcd_clear() #clear screen

#set the GPIO the sensor is connected to 
GPIO.setmode(GPIO.BCM)
my_gpio = 4 

#set the GPIO the switch is connected to
my_switch = 17
GPIO.setup(my_switch, GPIO.IN)
#GPIO.input(my_switch)
while start:
    try:
        my_lcd.lcd_display_string("Press the switch" , 1)

        if (GPIO.input(my_switch) == 0): #Freischalten
            my_lcd.lcd_clear()
            my_lcd.lcd_display_string("The application" , 1)
            my_lcd.lcd_display_string("is running" , 2)
            time.sleep(1)
            my_lcd.lcd_clear()
            
            while abbruch:
                try:
                    #read the humidity and temperature
                    my_humidity, my_temperature = Adafruit_DHT.read(my_sensor, my_gpio)

                    #change the data type
                    my_humidity_string = str(my_humidity) 
                    my_temperature_string = str(my_temperature)
                        
                        #control of reading
                    if my_humidity is not None and my_temperature is not None:
                        my_lcd.lcd_display_string("Temp: " + my_temperature_string + " C" , 1) #shows the temperature in line one
                        my_lcd.lcd_display_string("Humidity: " + my_humidity_string + " %" , 2) #shows the humidity in line two
                        time.sleep(5)
                        my_lcd.lcd_clear()
                        my_lcd.lcd_display_string("    Good Bye    " , 1)
                        time.sleep(2)
                        my_lcd.lcd_clear()
                        abbruch = False
                        start = False
                        break
                except ValueError:
                    my_lcd.lcd_display_string("Error," , 1)
                    my_lcd.lcd_display_string("try it again...")
                    time.sleep(2)
                    my_lcd.lcd_clear()
                    abbruch = True
    except ValueError:
        my_lcd.lcd_clear()
        my_lcd.lcd_display_string("Something goes" , 1)
        my_lcd.lcd_display_string("wrong" , 2)
        time.sleep(1)
        start = True

GPIO.cleanup()