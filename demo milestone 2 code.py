import time
import digitalio
import board
import adafruit_matrixkeypad

import pwmio
from adafruit_motor import servo

import neopixel


try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

def display():
    numpix = 16  
    pixpin = board.A1  
    strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.15)
    color = [255, 0, 0]

    circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    while True:
        for i in range(16):
            strip[circle[i]] = color
            strip[circle[(i + 8) % 16]] = [0, 0, 0]
            strip.write() 
            time.sleep(0.1)  

def reset():
    s1 = 120
    s2 = 60
    s3 = 90
    s4 = 90
    my_servo1.angle = s1 # left foot
    my_servo2.angle = s2 # right foot
    my_servo3.angle = s3 # left hip
    my_servo4.angle = s4 # right hip


def happy_feet():
    print("happy feet")
    count1 = 0
    while (count1 < 1):
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


        while (count2 != 5):

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
    while (count<1):
        my_servo1.angle = 120 # left foot
        my_servo2.angle = 60 # right foot
        my_servo3.angle = 90 # left hip
        my_servo4.angle = 90 # right hip
        for i in range(20):
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

    while (count<7):
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
    while (count <10):

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

spkrenable = digitalio.DigitalInOut(board.A2)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True
wave_file = open("laugh.wav", "rb")
wave = WaveFile(wave_file)
audio = AudioOut(board.A0)


cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D7, board.D5)]
rows = [digitalio.DigitalInOut(x) for x in (board.D13, board.D12, board.D11, board.D10)]

pwm1 = pwmio.PWMOut(board.D4, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.SCL, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm4 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm1) #left foot
my_servo2 = servo.Servo(pwm2) #right foot
my_servo3 = servo.Servo(pwm3) #left hip
my_servo3 = servo.Servo(pwm3) #left hip
my_servo4 = servo.Servo(pwm4) #right hip

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True:
    keys = keypad.pressed_keys
    if keys == [1]:
        audio.play(wave)
        while audio.playing:
            reset()
            happy_feet()
    time.sleep(0.1)

    if keys == [2]:
        audio.play(wave)
        while audio.playing:
            reset()
            jumping_jack()
    time.sleep(0.1)

    if keys == [4]:
        audio.play(wave)
        while audio.playing:
            reset()
            alpine()
    time.sleep(0.1)

    if keys == [5]:
        audio.play(wave)
        while audio.playing:
            reset()
            foot_swivel()
    time.sleep(0.1)

    if keys == [7]:
        audio.play(wave)
        while audio.playing:
            reset()
            tyson_dance()
    time.sleep(0.1)

    if keys == [8]:
        audio.play(wave)
        while audio.playing:
            reset()
            tbd_dance()
    time.sleep(0.1)

    if keys == ["*"]:
        reset() 
        print("empty")
        # buzzer_music
    time.sleep(0.1)

    if keys == [0]:
         
        display()
        print("empty")
    time.sleep(0.1)


