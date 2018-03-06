'''
author: Melanie Shimano
date: 03/06/2018
Controlling grow lights for SXSW EDU Hands On Session
Use with Raspberry Pi 3 and Python ver. 3.6

'''

#Python Code to turn lights on and off with raspberry pi GPIO pins

#import the GPIO and time packages

import RPi.GPIO as GPIO
import time

#setup GPIO pins and designate where we're attaching the lights (Pin 7 and GND)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)

#create a for loop to turn the light on and off automatically

for i in range(50): #for 50 days
    print('light on')
    GPIO.output(7, GPIO.HIGH) #turns the light on
    time.sleep(36000) #for 10 hours
    print('light off')
    GPIO.output(7, GPIO.LOW) #turns the light off
    time.sleep(54000) #for 14 hours

print("We're done playing with lights for now")
