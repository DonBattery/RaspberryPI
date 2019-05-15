#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

for i in range(0, 5):
    GPIO.output(4, True)
    time.sleep(0.5)
    GPIO.output(4, False)
    time.sleep(0.5)

GPIO.cleanup()
