import time

import board
import pulseio


#Define a list of tones/music notes to play.
TONE_FREQ = [
330, 330, 330, 262, 330, 392, 196, 262, 196, 165, 220, 247, 233, 220, 196, 330, 392,
440, 349, 392, 330, 262, 294, 247, 262, 196, 165, 220, 247, 233, 220, 196, 330, 392,
440, 349, 392, 330, 262, 294, 247, 392, 370, 330, 311, 330, 208, 220, 262, 220, 262,
294, 392, 370, 330, 311, 330, 523, 523, 523, 392, 370, 330, 311, 330, 208, 220, 262,
220, 262, 294, 311, 294, 262, 262, 262, 262, 262, 294, 330, 262, 220, 196, 262, 262,
262, 262, 294, 330, 262, 262, 262, 262, 294, 330, 262, 220, 196]

noteDurations = [
8,4,4,8,4,2,2,
3,3,3,4,4,8,4,8,8,8,4,8,4,3,8,8,3,
3,3,3,4,4,8,4,8,8,8,4,8,4,3,8,8,2,
8,8,8,4,4,8,8,4,8,8,3,8,8,8,4,4,4,8,2,
8,8,8,4,4,8,8,4,8,8,3,3,3,1,
8,4,4,8,4,8,4,8,2,8,4,4,8,4,1,
8,4,4,8,4,8,4,8,2
]

#Create piezo buzzer PWM output.
buzzer = pulseio.PWMOut(board.D5, variable_frequency=True)

buzzer.duty_cycle = 2**15  # 32768 value is 50% duty cycle, a square wave.

#Main loop will go through each tone in order up and down.
while True:
    for i in range(len(TONE_FREQ)):
        noteDuration = 800/noteDurations[i]
        buzzer.frequency = TONE_FREQ[i]*2
        time.sleep_ms(int(noteDuration * 1.30))
