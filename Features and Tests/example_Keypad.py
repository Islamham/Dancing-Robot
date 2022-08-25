import time
import digitalio
import board
import adafruit_matrixkeypad

import pwmio
from adafruit_motor import servo


def happy_feet():
    print("happy feet")
    count1 = 0
    while (count1 < 5):
        my_servo1.angle = 120 # left foot
        my_servo2.angle = 60 # right foot
        my_servo3.angle = 90 # left hip
        my_servo4.angle = 90 # right hip

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
        count1 += 1
        
def jumping_jack():
    print("jumping jack")
    count1 = 0
    count2 = 0
    while (count1 != 1):
        my_servo1.angle = 120 # left foot
        my_servo2.angle = 60 # right foot
        my_servo3.angle = 90 # left hip
        my_servo4.angle = 90 # right hip
        

        while (count2 != 10):

                my_servo1.angle -= 40
                my_servo2.angle += 40
                time.sleep(0.5)

                my_servo1.angle += 40
                my_servo2.angle -= 40
                time.sleep(0.5)
                count2 += 1
        count1 += 1

def alpine():
    print("alpine")
    count = 0
    while (count<10):
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

        count += 1

def foot_swivel():
    print("foot swivel")
    my_servo1.angle = 120  # left foot
    my_servo2.angle = 60  # right foot
    my_servo3.angle = 90  # left hip
    my_servo4.angle = 90  # right hip

    count = 0

    while (count<30):
        for angle in range(120, 90, -5):
            my_servo1.angle = angle

        # next 3 for loops is the right foot swivelling
        for i in range(3):
            for angle in range(90, 180, 5):
                my_servo4.angle = angle

            for angle in range(180, 90, -5):
                my_servo4.angle = angle

        for angle in range(90, 120, 5):
            my_servo1.angle = angle

        count += 1

def tyson_dance():
    print("tyson_dance")

    count = 0
    while (count <30):

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
        count += 1

def tbd_dance():
    print("tbd_dance")
    servo1 = 120
    servo2 = 60
    servo3 = 90
    servo4 = 90

    count = 0

    while (count<30):
        for angle in range(6):
            servo1 += 10
            my_servo1.angle = servo1
            time.sleep(.1)
        for angle in range(4):
            servo1 -= 15
            servo4 += 5
            my_servo1.angle = servo1
            my_servo4.angle = servo4
            time.sleep(.1)
        for angle in range(2):
            servo4 -= 20
            servo3 -= 5
            servo2 -= 10
            my_servo4.angle = servo4
            my_servo3.angle = servo3
            my_servo2.angle = servo2
            time.sleep(.1)
        for angle in range(2):
            servo4 -= 15
            my_servo4.angle = servo4
            time.sleep(.1)
        for angle in range(5):
            servo4 += 10
            my_servo4.angle = servo4
            time.sleep(.1)
        for angle in range(2):
            servo2 += 10
            my_servo2.angle = servo2
            time.sleep(.1)
        for angle in range(2):
            servo3 += 5
            servo2 += 5
            servo1 += 20
            my_servo3.angle = servo3
            my_servo2.angle = servo2
            my_servo1.angle = servo1
            time.sleep(.1)
        for angle in range(2):
            servo2 -= 5
            servo1 -= 20
            my_servo2.angle = servo2
            my_servo1.angle = servo1
            time.sleep(.1)
        count+=1



cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D7, board.D5)]
rows = [digitalio.DigitalInOut(x) for x in (board.D13, board.D12, board.D11, board.D10)]

pwm1 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm4 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm1) #left foot
my_servo2 = servo.Servo(pwm2) #right foot
my_servo3 = servo.Servo(pwm3) #left hip
my_servo4 = servo.Servo(pwm4) #right hip

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True:
    keys = keypad.pressed_keys
    if keys == [1]:
        happy_feet()
    time.sleep(0.1)
    
    if keys == [2]:
        jumping_jack()
    time.sleep(0.1)

    if keys == [4]:
        alpine()
    time.sleep(0.1)

    if keys == [5]:
        foot_swivel()
    time.sleep(0.1)

    if keys == [7]:
        tyson_dance()
    time.sleep(0.1)

    if keys == [8]:
        # dance move?
        tbd_dance()
    time.sleep(0.1)

    if keys == ["*"]:
        print("empty")
        # buzzer_music
    time.sleep(0.1)

    if keys == [0]:
        # last LCD?
        print("empty")
    time.sleep(0.1)


