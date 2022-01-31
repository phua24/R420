#!/usr/bin/env python3
########################################################################
# Filename    : MatrixKeypad.py
# Description : obtain the key code of 4x4 Matrix Keypad
# Author      : freenove
# modification: 2018/08/03
########################################################################
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)

GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)

try:
    GPIO.output(7, GPIO.LOW)
    print("First Relay is ON")
    time.sleep(5)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(11, GPIO.LOW)
    print("Second Relay is ON")
    time.sleep(5)
    GPIO.output(11, GPIO.High)
    time.sleep(1)
    GPIO.cleanup()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, exit the program.
    GPIO.cleanup()
