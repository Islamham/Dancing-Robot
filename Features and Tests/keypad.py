import time
import digitalio
import board
import adafruit_matrixkeypad

import board
import pwmio
from adafruit_motor import servo

def happy_feet():

    while True:
    	# stand on the outer sides of the feet (by 30 degrees from neutral)
        for i in range(7):
            my_servo1.angle = 120 - 5*i	# left foot, starts at 120
            my_servo2.angle = 60 - 5*i	# right foot, starts at 60

    	# rotate to the right
        for i in range(7):
            my_servo3.angle = 90 + 5*i  # left hip, starts at 90
            my_servo4.angle = 90 + 5*i 	# right hip, starts at 90

    	# undo above for loop
        for i in range(7):
            my_servo3.angle = 120 - 5*i
            my_servo4.angle = 120 - 5*i


    	# rotate to the right
        for i in range(7):
            my_servo3.angle = 90 + 5*i  # left hip, starts at 90
            my_servo4.angle = 90 + 5*i 	# right hip, starts at 90

    	# undo above for loop
        for i in range(7):
            my_servo3.angle = 120 - 5*i
            my_servo4.angle = 120 - 5*i

    	# undo first for loop
        for i in range(7):
            my_servo1.angle = 90 + 5*i
            my_servo2.angle = 30 + 5*i

    	# SECOND PART
    	# stand on the outer sides of the feet (by 30 degrees from neutral)
        for i in range(7):
            my_servo1.angle = 120 + 5*i	# left foot, starts at 120
            my_servo2.angle = 60 + 5*i	# right foot, starts at 60

        for i in range(7):
            my_servo3.angle = 90 - 5*i  # left hip, starts at 90
            my_servo4.angle = 90 - 5*i 	# right hip, starts at 90

        for i in range(7):
            my_servo3.angle = 60 + 5*i  # left hip, starts at 90
            my_servo4.angle = 60 + 5*i 	# right hip, starts at 90

        for i in range(7):
            my_servo3.angle = 90 - 5*i  # left hip, starts at 90
            my_servo4.angle = 90 - 5*i 	# right hip, starts at 90

        for i in range(7):
            my_servo3.angle = 60 + 5*i  # left hip, starts at 90
            my_servo4.angle = 60 + 5*i 	# right hip, starts at 90

        for i in range(7):
            my_servo1.angle = 150 - 5*i	# left foot, starts at 120
            my_servo2.angle = 90 - 5*i	# right foot, starts at 60

def alpine():


    while True:
        my_servo1.angle = 120 # left foot
        my_servo2.angle = 60 # right foot
        my_servo3.angle = 90 # left hip
        my_servo4.angle = 90 # right hip

        for i in range(50):
            my_servo3.angle += 20
            time.sleep(0.1)
            my_servo4.angle -= 20
            time.sleep(0.1)

            my_servo1.angle -= 15
            my_servo2.angle += 15
            time.sleep(0.1)

            my_servo3.angle -= 20
            time.sleep(0.1)
            my_servo4.angle += 20
            time.sleep(0.1)

            my_servo1.angle += 15
            my_servo2.angle -= 15
            time.sleep(0.1)

            my_servo3.angle -= 20
            time.sleep(0.1)
            my_servo4.angle += 20
            time.sleep(0.1)

            my_servo1.angle += 15
            my_servo2.angle -= 15
            time.sleep(0.1)

            my_servo3.angle += 20
            time.sleep(0.1)
            my_servo4.angle -= 20
            time.sleep(0.1)

            my_servo1.angle -= 15
            my_servo2.angle += 15
            time.sleep(0.1)

def foot_swivel():


    while True:
        for angle in range(120, 90, -5):
            my_servo1.angle = angle

        # next 3 for loops is the right foot swivelling
        for i in range(3):
            for angle in range(90, 180, 5):
                my_servo4.angle = angle

            for angle in range(180, 40, -5):
                my_servo4.angle = angle

            for angle in range(40, 90, 5):
                my_servo1.angle = angle

        for angle in range(90, 120, 5):
            my_servo1.angle = angle

def jumpingJack():


    while True:
        my_servo1.angle = 120 # left foot
        my_servo2.angle = 60 # right foot
        my_servo3.angle = 90 # left hip
        my_servo4.angle = 90 # right hip

        while True:

            my_servo1.angle -= 40
            my_servo2.angle += 40
            time.sleep(0.5)

            my_servo1.angle += 40
            my_servo2.angle -= 40
            time.sleep(0.5)

# pinouts
cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D7, board.D5)]
rows = [digitalio.DigitalInOut(x) for x in (board.D13, board.D12, board.D11, board.D10)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

pwm1 = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D4, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
pwm4 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm1) #left foot
my_servo2 = servo.Servo(pwm2) #right foot
my_servo3 = servo.Servo(pwm3) #left hip
my_servo4 = servo.Servo(pwm4) #right hip

while True:
    keys = keypad.pressed_keys

    if keys == 1:
        # call tyson_dance

        pwm1 = pwmio.PWMOut(board.D4, duty_cycle=2 ** 15, frequency=50)
        pwm2 = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
        pwm3 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
        pwm4 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)

        # Create a servo object, my_servo.
        my_servo1 = servo.Servo(pwm1)  #left foot
        my_servo2 = servo.Servo(pwm2)  #right foot
        my_servo3 = servo.Servo(pwm3)  #left hip
        my_servo4 = servo.Servo(pwm4)  #right hip

        while True:
            #my_servo1.angle = 125 # left foot
            #my_servo2.angle = 60 # right foot
            #my_servo3.angle = 90 # left hip
            #my_servo4.angle = 110 # right hip

            for angle in range(7):
                my_servo2.angle = 60 + (60/7)*angle
                my_servo1.angle = 125 + (25/7)*angle
                my_servo4.angle = 110 - (60/7)*angle

            for angle in range(10):
                my_servo2.angle = 120 - (85/10)*angle
                my_servo1.angle = 150 - (105/10)*angle
                my_servo3.angle = 90 - (30/10)*angle
                my_servo4.angle = 50 + (30/10)*angle

            for angle in range(7):
                my_servo4.angle = 80 + (30/7)*angle
                my_servo3.angle = 60 + (30/7)*angle
                my_servo2.angle = 35 + (25/7)*angle
                my_servo1.angle = 45 + (80/7)*angle

    if keys == 2:
        # call happy_feet
        happy_feet()

    if keys == 3:
        # call alpine
        alpine()

    if keys == 4:
        # call foot_swivel
        foot_swivel()

    if keys == 5:
        # call jumpingJack
        jumpingJack()

    if keys == 6:
        # call danceMove6()
        print("Pressed: ", keys)
        time.sleep(0.1)
    if keys == 7:
        print("Pressed: ", keys)
        time.sleep(0.1)
    if keys == 8:
        print("Pressed: ", keys)
        time.sleep(0.1)
    if keys == 9:
        print("Pressed: ", keys)
        time.sleep(0.1)
    if keys == "*":
        print("Pressed: ", keys)
        time.sleep(0.1)
    if keys == 0:
        print("Pressed: ", keys)
        time.sleep(0.1)
    if keys == "#":
        print("Pressed: ", keys)
        time.sleep(0.1)