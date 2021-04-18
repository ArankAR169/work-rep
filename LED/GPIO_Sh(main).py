import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

chan_list=[21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(chan_list, GPIO.OUT)

def lightUp(ledNumber, period):
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)

def blink(ledNumber, blinkCount, blinkPeriod):
    GPIO.setup(ledNumber, GPIO.OUT)
    for i in range(blinkCount+1):
        GPIO.output(ledNumber, 1)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber, 0)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    b=1000
    for i in range(count):
        if b==128 or b==1000:
            b=1
        else:
            b=b<<1
        b1=bin(b)[2:].zfill(8)
        c=[int(j) for j in b1]
        if len(c)==9:
            c.pop()
        GPIO.output(21, c[0])
        GPIO.output(20, c[1])
        GPIO.output(16, c[2])
        GPIO.output(12, c[3])
        GPIO.output(7, c[4])
        GPIO.output(8, c[5])
        GPIO.output(25, c[6])
        GPIO.output(24, c[7])
        time.sleep(period)
    GPIO.output(21, 0)
    GPIO.output(20, 0)
    GPIO.output(16, 0)
    GPIO.output(12, 0)
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(25, 0)
    GPIO.output(24, 0)

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
    GPIO.output(21, 0)
    GPIO.output(20, 0)
    GPIO.output(16, 0)
    GPIO.output(12, 0)
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(25, 0)
    GPIO.output(24, 0)

def decToBinList(decNumber):
    a=bin(decNumber)[2:].zfill(8)
    b=[i for i in a]
    print(b)

def lightNumber(number):
    a=bin(number)[2:].zfill(8)
    c=[int(i) for i in a]
    GPIO.output(21, c[0])
    GPIO.output(20, c[1])
    GPIO.output(16, c[2])
    GPIO.output(12, c[3])
    GPIO.output(7, c[4])
    GPIO.output(8, c[5])
    GPIO.output(25, c[6])
    GPIO.output(24, c[7])
    print('do not mentioned in task, but not to make program run infinitely will be disabled in 15 seconds')
    time.sleep(15)
    GPIO.output(21, 0)
    GPIO.output(20, 0)
    GPIO.output(16, 0)
    GPIO.output(12, 0)
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(25, 0)
    GPIO.output(24, 0)

# def runningPattern(pattern, direction):
#     a=bin(pattern)[2:].zfill(8)
#     c=[int(i) for i in a]
#     GPIO.output(21, c[0])
#     GPIO.output(20, c[1])
#     GPIO.output(16, c[2])
#     GPIO.output(12, c[3])
#     GPIO.output(7, c[4])
#     GPIO.output(8, c[5])
#     GPIO.output(25, c[6])
#     GPIO.output(24, c[7])
#     time.sleep(1)
#     if direction=='left':
#         While True:
#             a.append(a[0])
#             a.pop(0)
#             GPIO.output(21, c[0])
#             GPIO.output(20, c[1])
#             GPIO.output(16, c[2])
#             GPIO.output(12, c[3])
#             GPIO.output(7, c[4])
#             GPIO.output(8, c[5])
#             GPIO.output(25, c[6])
#             GPIO.output(24, c[7])
#             time.sleep(1)