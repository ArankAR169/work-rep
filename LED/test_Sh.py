import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

chan_list=[21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(chan_list, GPIO.OUT)

def runningDark(count, period):
    d=0
    bz=254
    b1=bin(bz)[2:10].zfill(8)
    c=[int(j) for j in b1]
    for i in range(count):
        GPIO.output(21, c[0])
        GPIO.output(20, c[1])
        GPIO.output(16, c[2])
        GPIO.output(12, c[3])
        GPIO.output(7, c[4])
        GPIO.output(8, c[5])
        GPIO.output(25, c[6])
        GPIO.output(24, c[7])
        time.sleep(period)
        if d==7:
            d=0
        else:
            d+=1
        b=bz-2**d+1
        b1=bin(b)[2:10].zfill(8)
        c=[int(j) for j in b1]
    GPIO.cleanup()

runningDark(10, 0.5)