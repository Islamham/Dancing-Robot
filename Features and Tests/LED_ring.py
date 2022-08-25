import time
import board
import neopixel

def display():
    numpix = 16  
    pixpin = board.A1  
    strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.15)
    color = [255, 0, 0]

    circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    while True:
        for i in range(circle.length):
            strip[circle[i]] = color
            strip[circle[(i + 8) % 16]] = [0, 0, 0]
            strip.write() 
            time.sleep(0.1)  