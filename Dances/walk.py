# walk

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

colours = [[69, 69, 255], [100, 255, 100], [255, 215, 0], [33, 100, 33], [22, 11, 100]] #array for LED colours

class WALK:

    def walk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):
        print("walk")
        count = 0
        while (count<1):
            #neutral position for servos
            s1 = 120 #left foot 
            s2 = 60 #right foot
            s3 = 90 #left hip
            s4 = 90 #right hip
            
            my_servo1.angle = s1 # left foot assignment 
            my_servo2.angle = s2 # right foot assignmet
            my_servo3.angle = s3 # left hip assignment
            my_servo4.angle = s4 # right hip assignment 


            # repeat the process below 5 times
            for i in range(5):
                strip.fill(colours[int(i % 5)]) #set all LEDs to colour determined by i 
                strip.write() #turns LEDs to last set colour

                # rotate right hip and left hip inward to make the feet head forward
                my_servo3.angle += 20
                time.sleep(0.1)
                my_servo4.angle -= 20
                time.sleep(0.1)

                # the slightly up lifted feet face down to the surface
                my_servo1.angle -= 15
                my_servo2.angle += 15
                time.sleep(0.1)
                

                # The right hip and left hip move back to the original position
                my_servo3.angle -= 20
                time.sleep(0.1)
                my_servo4.angle += 20
                time.sleep(0.1)

                # Both feet also move back to original position
                my_servo1.angle += 15
                my_servo2.angle -= 15
                time.sleep(0.1)
                
                # right hip and left hip rotate to outward to make the feet heading backward
                my_servo3.angle -= 20
                time.sleep(0.1)
                my_servo4.angle += 20
                time.sleep(0.1)

                # Since both feet's heels are lifted, place them down
                my_servo1.angle += 15
                my_servo2.angle -= 15
                time.sleep(0.1)
                
                # move the right hip and left hip back to the original standing position
                my_servo3.angle += 20
                time.sleep(0.1)
                my_servo4.angle -= 20
                time.sleep(0.1)

                # make the feet in original standing position.
                my_servo1.angle -= 15
                my_servo2.angle += 15
                time.sleep(0.1)

                count += 1