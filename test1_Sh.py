import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

chan_list=[21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(chan_list, GPIO.OUT)

GPIO.output(21, 0)
GPIO.output(20, 0)
GPIO.output(16, 0)
GPIO.output(12, 0)
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(25, 0)
GPIO.output(24, 0)

GPIO.cleanup()