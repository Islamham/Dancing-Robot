""" HAPPY FEET: lift left heel and right toe, point left heel and 
right toe right, come back, switch heels/toes, go left, reset. """

#Main Imports
import time
import digitalio
import board
import pwmio

#Keypad Import
import adafruit_matrixkeypad

#Servo Import
from adafruit_motor import servo

#LED Import
import neopixel

circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for indexes of LEDs

colours = [[148, 0, 211], [75, 0, 130], [0, 0, 255], [0, 255, 0], [255, 255, 0], [255, 127, 0], [255, 0, 0]] #array for LED colours

class HAPPY_FEET:
	def happy_feet(numpix, strip ,my_servo1, my_servo2, my_servo3, my_servo4):

		#neutral position for servos
		s1 = 120 #left foot 
		s2 = 60 #right foot
		s3 = 90 #left hip
		s4 = 90 #right hip

		my_servo1.angle = s1 # left foot assignment 
		my_servo2.angle = s2 # right foot assignmet
		my_servo3.angle = s3 # left hip assignment
		my_servo4.angle = s4 # right hip assignment 

		count1 = 0 #initiate count of dance move repititions
		while (count1 < 1): #while dance move has fully run less than once

			# stand on the left sides of the feet 
			for i in range(7):
				my_servo1.angle = s1 - 5*i	# left foot, starts at s1
				my_servo2.angle = s2 - 5*i	# right foot, starts at s2 
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour
				
			# rotate both hips to the right
			for i in range(7):
				my_servo3.angle = s3 + 5*i  # left hip, starts at s3
				my_servo4.angle = s4 + 5*i 	# right hip, starts at s4
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour
				
			# rotate both hips back to neutral position
			for i in range(7):
				my_servo3.angle = (s3+30) - 5*i	#left hip, returning to s3
				my_servo4.angle = (s4+30) - 5*i #right hip, returning to s4
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour
				
			# rotate both hips to the right
			for i in range(7):
				my_servo3.angle = s3 + 5*i  # left hip, starts at s3
				my_servo4.angle = s4 + 5*i 	# right hip, starts at s4
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour
				
			# rotate both hips back to neutral position
			for i in range(7):
				my_servo3.angle = (s3+30) - 5*i	#left hip, returning to s3
				my_servo4.angle = (s4+30) - 5*i #right hip, returning to s4
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour
				
			# tilt both feet back to their neutral position
			for i in range(7):
				my_servo1.angle = (s1-30) + 5*i #left foot, returning to s1
				my_servo2.angle = (s2-30) + 5*i #right foot, returning to s2
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour

			# SECOND PART
			# stand on the right sides of the feet 
			for i in range(7):
				my_servo1.angle = s1 + 5*i	# left foot, starts at s1
				my_servo2.angle = s2 + 5*i	# right foot, starts at s2
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour

			# rotate both hips to the left
			for i in range(7):
				my_servo3.angle = s3 - 5*i  # left hip, starts at s3
				my_servo4.angle = s4 - 5*i 	# right hip, starts at s4
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour

			# rotate both hips back to neutral position
			for i in range(7):
				my_servo3.angle = (s3-30) + 5*i  # left hip, returning to s3
				my_servo4.angle = (s4-30) + 5*i 	# right hip, returning to s4
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour

			# rotate both hips to the left
			for i in range(7):
				my_servo3.angle = s3 - 5*i  # left hip, starts at s3
				my_servo4.angle = s4 - 5*i 	# right hip, starts at s4
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour

			# rotate both hips back to neutral position
			for i in range(7):
				my_servo3.angle = (s3-30) + 5*i  # left hip, returning to s3
				my_servo4.angle = (s4-30) + 5*i 	# right hip, returning to s4
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour

			# tilt both feet back to their neutral position
			for i in range(7):
				my_servo1.angle = (s1+30) - 5*i	# left foot, returning to s1
				my_servo2.angle = (s2+30) - 5*i	# right foot, returning to s2
				strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
				strip.write() #turns LEDs to last set colour

			count1 += 1 #increment count
				
			