'''
Need to change the localization options


'''
import time
import datetime
from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address = 0x70)

segment.begin()

print("Press CTRL + Z to exit")

#Continuously update the time on a 4 char.
try:
	while(True):
		now = datetime.datetime.now()
		hour = now.hour
		minute = now.minute
		second = now.second

		segment.clear()

		#Set hours
		segment.set_digit(0, int(hour / 10))	#Tens
		segment.set_digit(1, hour % 10)			#Ones

		#Set Minutes
		segment.set_digit(2, int(minute / 10))	#Tens
		segment.set_digit(3, minute % 10)		#Ones

		#Toggle Colon
		segment.set_colon(second % 2)			#Toggle colon as 1Hz

		#Write the display buffer to the hardware. This must be called to
		#update the actual display LEDs.

		segment.write_display()

		#Wait a quarter second (less than 1 second to prevent colon blinking getting$)
		time.sleep(0.25)

except KeyboardInterupt:
	segment.clear()
	segment.write_display()


