#!/usr/bin/env python3
########################################################################
# Filename    : MatrixKeypad.py
# Description : obtain the key code of 4x4 Matrix Keypad
# Author      : freenove
# modification: 2018/08/03
########################################################################
import RPi.GPIO as GPIO
import Keypad  # import module Keypad


try:
    print("test")
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, exit the program.
    GPIO.cleanup()
