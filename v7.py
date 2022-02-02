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

GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.HIGH)

try:
    GPIO.output(13, GPIO.LOW)
    print("Third Relay is ON")

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, exit the program.
    GPIO.cleanup()
