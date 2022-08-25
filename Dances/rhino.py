""" TO BE NAMED """
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

circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for indexes of LEDs


class RHINO:
    def rhino(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):
        print("rhino")
        
        my_servo1.angle = 120 # left foot assignment 
        my_servo2.angle = 60 # right foot assignmet
        my_servo3.angle = 90 # left hip assignment
        my_servo4.angle = 90 # right hip assignment 

        #neutral position for servos
        servo1 = 120 #left foot 
        servo2 = 60 #right foot
        servo3 = 90 #left hip
        servo4 = 90 #right hip
        
        count = 0 #initialize count to zero

        while (count<1):
            strip.fill([0, 0, 0])
            strip.write()
            x = 0

            #first section
            for angle in range(6):
                servo1 += 10 #incrememnt angle for left foot 
                my_servo1.angle = servo1 #set angle of left foot
                strip[circle[x]] = [255, 255, 0] #set LED at index x = 0
                x += 1 #increment x 
                strip.write() #turn all LEDs to last set colour
                time.sleep(.1) #sleep for 100 milliseconds
            for angle in range(4):
                servo1 -= 15 #decrememnt angle for left foot
                servo4 += 5 #incrememnt angle for left foot
                my_servo1.angle = servo1 #set angle for left foot 
                my_servo4.angle = servo4 #set angle for left foot
                strip[circle[x]] = [255, 255, 0] #set LED at index x = 0
                x += 1 #increment x 
                strip.write() #turn all LEDs to last set colour
                time.sleep(.1) #sleep for 100 milliseconds
            for angle in range(2):
                strip[circle[x]] = [255, 255, 0] #set LED at index x = 0
                x += 1 #increment x 
                strip.write() #turn all LEDs to last set colour
                servo4 -= 20 #decrememnt angle for right hip
                servo3 -= 5 #decrememnt angle for left hip
                servo2 -= 10 #decrememnt angle for right foot
                my_servo4.angle = servo4 #set angle for right hip
                my_servo3.angle = servo3 #set angle for left hip
                my_servo2.angle = servo2 #set angle for right foot
                strip[circle[x]] = [255, 255, 0] #set LED at index x = 0
                x += 1 #increment x 
                strip.write() #turn all LEDs to last set colour
                time.sleep(.1) #sleep for 100 milliseconds
            for angle in range(2):
                servo4 -= 15 #decrememnt angle for right hip
                my_servo4.angle = servo4 #set angle for right hip
                time.sleep(.1) #sleep for 100 milliseconds

            #second section
            for angle in range(5):
                if angle % 2 == 0: #if angle % 2 == 0, then set red on LEDs, else set white on LEDs
                    strip.fill([255, 0, 0])
                else:
                    strip.fill([255, 255, 255])
                strip.write() #turn all LEDs to last set colour
                servo4 += 10 #incrememnt angle for right hip
                my_servo4.angle = servo4 #set angle for right hip
                time.sleep(.1) #sleep for 100 milliseconds
            for angle in range(2):
                if angle % 2 == 0: #if angle % 2 == 0, then set red on LEDs, else set white on LEDs
                    strip.fill([255, 0, 0])
                else:
                    strip.fill([255, 255, 255])
                strip.write() #turn all LEDs to last set colour
                servo2 += 10 #incrememnt angle for right foot
                my_servo2.angle = servo2 #set angle for right foot
                time.sleep(.1) #sleep for 100 milliseconds
            for angle in range(2):
                if angle % 2 == 0: #if angle % 2 == 0, then set red on LEDs, else set white on LEDs
                    strip.fill([255, 0, 0])
                else:
                    strip.fill([255, 255, 255])
                strip.write() #turn all LEDs to last set colour
                servo3 += 5 #incrememnt angle for left hip
                servo2 += 5 #incrememnt angle for right foot
                servo1 += 20 #incrememnt angle for left foot
                my_servo3.angle = servo3 #set angle for left hip
                my_servo2.angle = servo2 #set angle for left foot
                my_servo1.angle = servo1 #set angle for left foot
                time.sleep(.1) #sleep for 100 milliseconds
            for angle in range(2):
                if angle % 2 == 0: #if angle % 2 == 0, then set red on LEDs, else set white on LEDs
                    strip.fill([255, 0, 0])
                else:
                    strip.fill([255, 255, 255])
                strip.write() #turn all LEDs to last set colour
                servo2 -= 5 #decrememnt angle for right foot
                servo1 -= 20 #decrememnt angle for left foot
                my_servo2.angle = servo2 #set angle for left foot
                my_servo1.angle = servo1 #set angle for left foot
                time.sleep(.1) #sleep for 100 milliseconds
            count+=1 #increment count