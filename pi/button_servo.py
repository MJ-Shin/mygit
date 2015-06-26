import time
import RPi.GPIO as GPIO

#GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup (20, GPIO.IN)	#button_yellow
GPIO.setup (18, GPIO.IN)	#button_red

count = 0
motor = GPIO.PWM(17,50)

motor.start(0)

yellow = GPIO.input(20)
red = GPIO.input(18)        

try :     
	while True:
		if (yellow == True):
			print("Yellow Pressed : OPEN")
			motor.ChangeDutyCycle(7.5)
                    	sleep (1) 
                if(red == True): 
			print("Red Pressed : CLOSE")
                	motor.ChangeDutyCycle(12.5)
			sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()

