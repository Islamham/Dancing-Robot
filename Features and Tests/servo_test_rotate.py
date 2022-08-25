### COPY CODE BELOW INTO code.py ON THE BOARD TO RUN IT ###

import time
import board
import pwmio
from adafruit_motor import servo

# 1 create a PWMOut object on Pin D10.
pwm1 = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
# 1 Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm1)

# 2 create a PWMOut object on Pin D11.
pwm2 = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=25)
# 2 Create a servo object, my_servo.
my_servo2 = servo.Servo(pwm2)

# 3 create a PWMOut object on Pin D12.
pwm3 = pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=30)
# 3 Create a servo object, my_servo.
my_servo3 = servo.Servo(pwm3)

# 4 create a PWMOut object on Pin D13.
pwm4 = pwmio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=40)
# 4 Create a servo object, my_servo.
my_servo4 = servo.Servo(pwm4)

while True:
    for angle in range(0, 90, 5):  # 0 - 90 degrees, 5 degrees at a time.
        my_servo1.angle = angle
        time.sleep(0.05)
    for angle in range(90, 0, -5):   # 90 - 0 degrees, 5 degrees at a time.
        my_servo1.angle = angle
        time.sleep(0.05)
    for angle in range(0, 90, 9):  # 0 - 90 degrees, 9 degrees at a time.
        my_servo2.angle = angle
        time.sleep(0.05)
    for angle in range(90, 0, -9):   # 90 - 0 degrees, 9 degrees at a time.
        my_servo2.angle = angle
        time.sleep(0.07)
    for angle in range(0, 90, 5):  # 0 - 90 degrees, 5 degrees at a time.
        my_servo3.angle = angle
        time.sleep(0.13)
    for angle in range(90, 0, -3):   # 90 - 0 degrees, 3 degrees at a time.
        my_servo3.angle = angle
        time.sleep(0.05)
    for angle in range(0, 90, 9):  # 0 - 90 degrees, 9 degrees at a time.
        my_servo4.angle = angle
        time.sleep(0.25)
    for angle in range(90, 0, -10):   # 90 - 0 degrees, 10 degrees at a time.
        my_servo4.angle = angle
        time.sleep(0.35)