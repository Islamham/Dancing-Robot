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

class MOONWALK:
    def moonwalk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):

    
        count = 0
        while (count <2): #while the dance move has run through less than twice

            #my_servo1.angle = 125 # left foot
            #my_servo2.angle = 60 # right foot
            #my_servo3.angle = 90 # left hip
            #my_servo4.angle = 110 # right hip

            for angle in range(8): #iterate angle from 0 -> 7
                my_servo2.angle = 60 + (60/8)*angle #rotate the right foot onto right edge
                my_servo1.angle = 125 + (25/8)*angle #rotate the left foot onto its right edge
                my_servo4.angle = 110 - (60/8)*angle #rotate right hip to the left

                strip[circle[int((angle + 0)%16)]] = [255,0,0] #set LED at index i to red
                strip[circle[int((angle + 1)%16)]] = [255,255,255] #set LED at index i + 1 to white
                strip[circle[int((angle + 8)%16)]] = [0,0,0] #set LED across from index i to black (off)
                strip[circle[int((angle + 9)%16)]] = [0,0,0] #set LED across from index i + 1 to black (off)
                strip.write() #turns LEDs to last set colour

            for angle in range(10):  
                my_servo2.angle = 120 - (85/10)*angle #rotate right foot onto its left edge
                my_servo1.angle = 150 - (105/10)*angle #rotate left foot onto its left edge
                my_servo3.angle = 90 - (30/10)*angle #rotate left hip to the left
                my_servo4.angle = 50 + (30/10)*angle #rotate right hip to the right
                if angle % 2 == 0: #if angle is even, flash red
                    strip.fill([255,0,0]) #set all LEDs to red
                    strip.write() #turns LEDs to last set colour
                else:
                    strip.fill([255,255,255]) #set all LEDs to white
                    strip.write() #turns LEDs to last set colour

            for angle in range(8):  
                my_servo4.angle = 80 + (30/8)*angle #rotate right hip to the right
                my_servo3.angle = 60 + (30/8)*angle #rotate left hip to the right 
                my_servo2.angle = 35 + (25/8)*angle #rotate right foot back to neutral position
                my_servo1.angle = 45 + (80/8)*angle #rotate left foot back to neutral position

                strip[circle[int((angle + 0)%16)]] = [0,0,0] #set LED at index i to black (off)
                strip[circle[int((angle + 1)%16)]] = [0,0,0] #set LED at index i + 1 to black (off)
                strip[circle[int((angle + 8)%16)]] = [255,0,0] #set LED across from index i to red
                strip[circle[int((angle + 9)%16)]] = [255,255,255] #set LED across from index i + 1 to white
                strip.write() #turns LEDs to last set colour
                
            count += 1 #increment count
