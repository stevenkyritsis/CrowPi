import RPi.GPIO as GPIO
import time

relay_pin = 40

#set GPIO mode as GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

#setup relay pin as output
GPIO.setup(relay_pin, GPIO.OUT)

#Open Relay
GPIO.output(relay_pin, GPIO.LOW)

#Wait half a second
time.sleep(1)

#Close Relay
GPIO.output(relay_pin, GPIO.HIGH)
GPIO.cleanup()
