# jumping jack

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

class JUMPING_JACK:
	def jumping_jack(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):

            count1 = 0 #count for inner loop set to 0
            count2 = 0 #count for outer loop fet to 0
            x = 0 #iterator for LED colour set to 0
            while (count1 != 1): # while inner loop has completed less than once

                #neutral position for servos
                s1 = 120 #left foot 
                s2 = 60 #right foot
                s3 = 90 #left hip
                s4 = 90 #right hip

                my_servo1.angle = s1 # left foot assignment 
                my_servo2.angle = s2 # right foot assignmet
                my_servo3.angle = s3 # left hip assignment
                my_servo4.angle = s4 # right hip assignment 

                while (count2 != 1): # while outer loop

                    # Both feet rotate to outward, so the robot standing with its toes.
                    my_servo1.angle -= 40 #rotate left foot onto its left edge
                    my_servo2.angle += 40 #rotate right foot onto its right edge

                   #run a rainbow swirl pattern around the ring LED, chain on 8 pixels
                    for i in range(16):
                        strip[circle[i]] = colours[int(x % 7)] #set an LED of index i to the colour determined by colours[x]
                        x += 1 #increment to next colour
                        strip[circle[int((i + 8) % 16)]] = [0, 0, 0] #set LED opposite of index i to black (off)
                        strip.write() #turn LEDs to last set colour
                        time.sleep(0.02) #sleep for 20 milliseconds
                        
                    # Move the toes in by rotating feet inward, so the robot standing as before.
                    my_servo1.angle += 40 #rotate left foot back to its neutral position
                    my_servo2.angle -= 40 #rotate right foot back to its neutral position

                    #run a rainbow swirl pattern around the ring LED, chain on 8 pixels
                    for i in range(16):
                        strip[circle[i]] = colours[int(x % 7)] #set an LED of index i to the colour determined by colours[x]
                        x += 1 #increment to next colour
                        strip[circle[int((i + 8) % 16)]] = [0, 0, 0] #set LED opposite of index i to black (off)
                        strip.write() #turn LEDs to last set colour
                        time.sleep(0.02) #sleep for 20 milliseconds

                    count2 += 1 #increment count for the inner loop
                count1 += 1 #increment count for the outer loop