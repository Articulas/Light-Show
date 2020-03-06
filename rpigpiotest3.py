import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT) # red
GPIO.setup(11,GPIO.OUT)# blue
GPIO.setup(13,GPIO.OUT)# yellow
GPIO.setup(15,GPIO.OUT)# Green
GPIO.setup(18,GPIO.OUT)# white

GPIO.setwarnings(False) # to disable warnings.


for x in range (0,25):

    GPIO.output(7,True)
    time.sleep(.05)
    GPIO.output(7,False)
    GPIO.output(11,True)
    time.sleep(.05)
    GPIO.output(11,False)
    GPIO.output(13,True)
    time.sleep(.05)
    GPIO.output(13,False)
    GPIO.output(15,True)
    time.sleep(.05)
    GPIO.output(15,False)
    GPIO.output(18,True)
    time.sleep(.05)
    GPIO.output(18,False)
    time.sleep(.05)

for y in range (0,25):

    GPIO.output(18,True)
    time.sleep(.05)
    GPIO.output(18,False)
    GPIO.output(15,True)
    time.sleep(.05)
    GPIO.output(15,False)
    GPIO.output(13,True)
    time.sleep(.05)
    GPIO.output(13,False)
    GPIO.output(11,True)
    time.sleep(.05)
    GPIO.output(11,False)
    GPIO.output(7,True)
    time.sleep(.05)
    GPIO.output(7,False)
    time.sleep(.05)    

for z in range (0,100):
    GPIO.output(7,True)
    time.sleep(.05)
    GPIO.output(7,False)
    GPIO.output(11,True)
    time.sleep(.05)
    GPIO.output(11,False)
    GPIO.output(13,True)
    time.sleep(.05)
    GPIO.output(13,False)
    GPIO.output(15,True)
    time.sleep(.05)
    GPIO.output(15,False)
    GPIO.output(18,True)
    time.sleep(.05)
    GPIO.output(18,False)
    time.sleep(.05)
    GPIO.output(18,True)
    time.sleep(.05)
    GPIO.output(18,False)
    GPIO.output(15,True)
    time.sleep(.05)
    GPIO.output(15,False)
    GPIO.output(13,True)
    time.sleep(.05)
    GPIO.output(13,False)
    GPIO.output(11,True)
    time.sleep(.05)
    GPIO.output(11,False)
    GPIO.output(7,True)
    time.sleep(.05)
    GPIO.output(7,False)
    time.sleep(.05)


GPIO.cleanup()
