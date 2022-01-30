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

MATRICK = [[1, 2, 3, 'A'],
           [4, 5, 6, 'B'],
           [7, 8, 9, 'C'],
           ['*', 0, '#', 'D']]

ROW = [7, 11, 13, 15]
COL = [12, 16, 18, 22]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN)

try:
    while True:
        for j in range(4):
            GPIO.output(COL[j], 0)

            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    print(COL[j])
                    print(Row[i])
                    print(MATRICK[i][j])
                    time.sleep(1)
                    while GPIO.input(ROW[i]) == 0:
                        pass
                GPIO.output(COL[i], 1)


except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, exit the program.
    GPIO.cleanup()
