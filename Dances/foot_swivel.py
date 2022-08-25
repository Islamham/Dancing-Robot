""" LIFT LEFT FOOT, SWIVEL RIGHT HIP, AND RESET """
 # (note: as of feb 17 at 10:20, this is untested)
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

#LCD Import
import tftlcd

class FOOT_SWIVEL:

    def foot_swivel(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):
        print("foot swivel") #print "foot swivel"

        # set reset states
        my_servo1.angle = 120  # left foot
        my_servo2.angle = 60  # right foot
        my_servo3.angle = 90  # left hip
        my_servo4.angle = 90  # right hip

        circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 15] #array for index of LED assignment

        count = 0 #count to control repetition of dance moves

        while (count<1): # while dance move has run less than once through 
            strip.fill([255,0,0]) #set all LEDs to red
            strip.write() #turn LEDs to last set colour

            for angle in range(120, 90, -5): #iterate angle from 120 to 90 in steps of -5
                my_servo1.angle = angle #tilts the left foot of the robot to the angle, angle, 

            # next 3 for loops is the right foot swivelling
            for i in range(3): #run the right toe swivel 3 times
                for angle in range(90, 180, 5): #iterate angle from 90 to 180 in steps of 5
                    my_servo4.angle = angle #rotates the robots right hip so that its right leg points further and further to the right
                    strip[circle[int((angle-90)/5)]] = [0,0,255] #over the duration of the loop, set one pixel at a time to blue in a rotating order
                    strip.write() #turn LEDs to last set colour


                for angle in range(180, 90, -5): #iterate angle from 180 to 90 in steps of -5
                    my_servo4.angle = angle #rotates the robots right hip so that its right leg points closer and closer to its original orientation
                    strip[circle[int((180-angle)/5)]] = [255,0,0] #over the duration of the loop, set one pixel at a time to red in a rotating order
                    strip.write() #turn LEDs to last set colour

            for angle in range(90, 120, 5): #iterate angle from 90 to 120 in steps of 5
                my_servo1.angle = angle #tilts the left foot of the robot back to its original position

            count += 1 #add 1 to count