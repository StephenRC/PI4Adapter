# uses https://www.amazon.com/gp/product/B08RDYDG6X
# RPi GPIO LED & Breakout board

import RPi.GPIO as GPIO
import time

led = [14,15,18,23,24,25,8,7,1,12,16,20,21,2,3,4,17,27,22,10,9,11,0,5,6,13,19,26]
y = True

GPIO.setmode(GPIO.BCM)
while y :
    for x in led:
        #print(x)
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(x, GPIO.LOW)
	print(y)
    y = y + 1
    if y > 5:
        y = False
GPIO.cleanup()
