import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pins.
pwm1 = pwmio.PWMOut(board.SCL, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D4, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
pwm4 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm1) #left foot
my_servo2 = servo.Servo(pwm2) #right foot
my_servo3 = servo.Servo(pwm3) #left hip
my_servo4 = servo.Servo(pwm4) #right hip

while True:
    my_servo1.angle = 120 # left foot
    my_servo2.angle = 60 # right foot
    my_servo3.angle = 90 # left hip
    my_servo4.angle = 90 # right hip
    
    #my_servo1.angle = 50 #MIN for left foot (Outer Foot)
    #my_servo1.angle = 120 # center left foot
    #my_servo1.angle = 180 #MAX for left foot (Inner Foot)

    #my_servo2.angle = 130 #MIN for right foot (Outer Foot)
    #my_servo2.angle = 60 # center right foot
    #my_servo2.angle = 0 #MAX for right foot (Inner Foot)

    #my_servo3.angle = 140 #MIN for left hip (Toes In)
    #my_servo3.angle = 90 # center left hip
    #my_servo3.angle = 0 #MAX for left hip (Toes Out)

    #my_servo4.angle = 40 #MIN for right hip (Toes In)
    #my_servo4.angle = 90 # center right hip
    #my_servo4.angle = 180 #MAX for right hip (Toes Out)
    
    
    #for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        #my_servo1.angle = angle
        #my_servo2.angle = angle
        #my_servo3.angle = angle
        #my_servo4.angle = 180 - angle
        #time.sleep(0.05)
    #for angle in range(180, 0, -5):   # 180 - 0 degrees, 5 degrees at a time.
        #my_servo1.angle = angle
        #my_servo2.angle = angle
        #my_servo3.angle = angle
        #my_servo4.angle = angle
        #time.sleep(0.05)
        