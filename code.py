#Main Imports
import time #used for sleep calls
import digitalio #used for digital input/output assignments
import board #used for board pin assignments
import pwmio #used to create pwm objects

#LCD Imports
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

#Keypad Import
import time
import digitalio
import board

# import adafruit_matrixkeypad
from digitalio import Direction, Pull

#Servo Import
from adafruit_motor import servo

#LED Import
import neopixel

#Speaker Imports
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

class FOOT_SWIVEL:

    def foot_swivel(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):
        print("foot swivel") #print "foot swivel"

        # set reset states
        my_servo1.angle = 120  # left foot
        my_servo2.angle = 60  # right foot
        my_servo3.angle = 90  # left hip
        my_servo4.angle = 90  # right hip

        circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 15] #array for index of LED assignment

        count = 0 #count to control repetition of dance moves

        while (count<1): # while dance move has run less than once through
            strip.fill([255,0,0]) #set all LEDs to red
            strip.write() #turn LEDs to last set colour

            for angle in range(120, 90, -5): #iterate angle from 120 to 90 in steps of -5
                my_servo1.angle = angle #tilts the left foot of the robot to the angle, angle,

            # next 3 for loops is the right foot swivelling
            for i in range(3): #run the right toe swivel 3 times
                for angle in range(90, 180, 5): #iterate angle from 90 to 180 in steps of 5
                    my_servo4.angle = angle #rotates the robots right hip so that its right leg points further and further to the right
                    strip[circle[int((angle-90)/5)]] = [0,0,255] #over the duration of the loop, set one pixel at a time to blue in a rotating order
                    strip.write() #turn LEDs to last set colour


                for angle in range(180, 90, -5): #iterate angle from 180 to 90 in steps of -5
                    my_servo4.angle = angle #rotates the robots right hip so that its right leg points closer and closer to its original orientation
                    strip[circle[int((180-angle)/5)]] = [255,0,0] #over the duration of the loop, set one pixel at a time to red in a rotating order
                    strip.write() #turn LEDs to last set colour

            for angle in range(90, 120, 5): #iterate angle from 90 to 120 in steps of 5
                my_servo1.angle = angle #tilts the left foot of the robot back to its original position

            count += 1 #add 1 to count


class HAPPY_FEET:

    circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for indexes of LEDs
    colours = [[148, 0, 211], [75, 0, 130], [0, 0, 255], [0, 255, 0], [255, 255, 0], [255, 127, 0], [255, 0, 0]] #array for LED colours
	
    def happy_feet(numpix, strip ,my_servo1, my_servo2, my_servo3, my_servo4):

        circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for indexes of LEDs
        colours = [[148, 0, 211], [75, 0, 130], [0, 0, 255], [0, 255, 0], [255, 255, 0], [255, 127, 0], [255, 0, 0]] #array for LED colours

        #neutral position for servos
        s1 = 120 #left foot
        s2 = 60 #right foot
        s3 = 90 #left hip
        s4 = 90 #right hip

        my_servo1.angle = s1 # left foot assignment
        my_servo2.angle = s2 # right foot assignmet
        my_servo3.angle = s3 # left hip assignment
        my_servo4.angle = s4 # right hip assignment



        count1 = 0 #initiate count of dance move repititions
        while (count1 < 1): #while dance move has fully run less than once

            # stand on the left sides of the feet
            for i in range(7):
                my_servo1.angle = s1 - 5*i	# left foot, starts at s1
                my_servo2.angle = s2 - 5*i	# right foot, starts at s2
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # rotate both hips to the right
            for i in range(7):
                my_servo3.angle = s3 + 5*i  # left hip, starts at s3
                my_servo4.angle = s4 + 5*i 	# right hip, starts at s4
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # rotate both hips back to neutral position
            for i in range(7):
                my_servo3.angle = (s3+30) - 5*i	#left hip, returning to s3
                my_servo4.angle = (s4+30) - 5*i #right hip, returning to s4
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # rotate both hips to the right
            for i in range(7):
                my_servo3.angle = s3 + 5*i  # left hip, starts at s3
                my_servo4.angle = s4 + 5*i 	# right hip, starts at s4
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # rotate both hips back to neutral position
            for i in range(7):
                my_servo3.angle = (s3+30) - 5*i	#left hip, returning to s3
                my_servo4.angle = (s4+30) - 5*i #right hip, returning to s4
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # tilt both feet back to their neutral position
            for i in range(7):
                my_servo1.angle = (s1-30) + 5*i #left foot, returning to s1
                my_servo2.angle = (s2-30) + 5*i #right foot, returning to s2
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # SECOND PART
            # stand on the right sides of the feet
            for i in range(7):
                my_servo1.angle = s1 + 5*i	# left foot, starts at s1
                my_servo2.angle = s2 + 5*i	# right foot, starts at s2
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # rotate both hips to the left
            for i in range(7):
                my_servo3.angle = s3 - 5*i  # left hip, starts at s3
                my_servo4.angle = s4 - 5*i 	# right hip, starts at s4
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # rotate both hips back to neutral position
            for i in range(7):
                my_servo3.angle = (s3-30) + 5*i  # left hip, returning to s3
                my_servo4.angle = (s4-30) + 5*i 	# right hip, returning to s4
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # rotate both hips to the left
            for i in range(7):
                my_servo3.angle = s3 - 5*i  # left hip, starts at s3
                my_servo4.angle = s4 - 5*i 	# right hip, starts at s4
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # rotate both hips back to neutral position
            for i in range(7):
                my_servo3.angle = (s3-30) + 5*i  # left hip, returning to s3
                my_servo4.angle = (s4-30) + 5*i 	# right hip, returning to s4
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            # tilt both feet back to their neutral position
            for i in range(7):
                my_servo1.angle = (s1+30) - 5*i	# left foot, returning to s1
                my_servo2.angle = (s2+30) - 5*i	# right foot, returning to s2
                strip.fill(colours[int(i)]) #sets all LEDs to colours specified by i in colours
                strip.write() #turns LEDs to last set colour

            count1 += 1 #increment count


class JUMPING_JACK:

	
    def jumping_jack(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):
            circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for indexes of LEDs

            colours = [[148, 0, 211], [75, 0, 130], [0, 0, 255], [0, 255, 0], [255, 255, 0], [255, 127, 0], [255, 0, 0]] #array for LED colours

            count1 = 0 #count for inner loop set to 0
            count2 = 0 #count for outer loop fet to 0
            x = 0 #iterator for LED colour set to 0
            while (count1 != 1): # while inner loop has completed less than once

                #neutral position for servos
                s1 = 120 #left foot
                s2 = 60 #right foot
                s3 = 90 #left hip
                s4 = 90 #right hip

                my_servo1.angle = s1 # left foot assignment
                my_servo2.angle = s2 # right foot assignmet
                my_servo3.angle = s3 # left hip assignment
                my_servo4.angle = s4 # right hip assignment

                while (count2 != 1): # while outer loop

                    # Both feet rotate to outward, so the robot standing with its toes.
                    my_servo1.angle -= 40 #rotate left foot onto its left edge
                    my_servo2.angle += 40 #rotate right foot onto its right edge

                   #run a rainbow swirl pattern around the ring LED, chain on 8 pixels
                    for i in range(16):
                        strip[circle[i]] = colours[int(x % 7)] #set an LED of index i to the colour determined by colours[x]
                        x += 1 #increment to next colour
                        strip[circle[int((i + 8) % 16)]] = [0, 0, 0] #set LED opposite of index i to black (off)
                        strip.write() #turn LEDs to last set colour
                        time.sleep(0.02) #sleep for 20 milliseconds

                    # Move the toes in by rotating feet inward, so the robot standing as before.
                    my_servo1.angle += 40 #rotate left foot back to its neutral position
                    my_servo2.angle -= 40 #rotate right foot back to its neutral position

                    #run a rainbow swirl pattern around the ring LED, chain on 8 pixels
                    for i in range(16):
                        strip[circle[i]] = colours[int(x % 7)] #set an LED of index i to the colour determined by colours[x]
                        x += 1 #increment to next colour
                        strip[circle[int((i + 8) % 16)]] = [0, 0, 0] #set LED opposite of index i to black (off)
                        strip.write() #turn LEDs to last set colour
                        time.sleep(0.02) #sleep for 20 milliseconds

                    count2 += 1 #increment count for the inner loop
                count1 += 1 #increment count for the outer loop	

class MOONWALK:
    def moonwalk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):

        circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for indexes of LEDs

        count = 0
        while (count <1): #while the dance move has run through less than once

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


class RHINO:
    def rhino(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):

        circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for indexes of LEDs

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


class WALK:

    def walk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4):
        circle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for indexes of LEDs
        colours = [[69, 69, 255], [100, 255, 100], [255, 215, 0], [33, 100, 33], [22, 11, 100]] #array for LED colours
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


            # repeat the process below 20 times
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

class LCD:
    def __init__(self):
        displayio.release_displays()

        self.spi = board.SPI()
        self.tft_cs = board.A4
        self.tft_dc = board.A3
        self.reset = board.A5

        self.display_bus = displayio.FourWire(
            self.spi, command=self.tft_dc, chip_select=self.tft_cs, reset=self.reset
        )

        self.display = ST7735R(self.display_bus, width=128, height=128, colstart=2, rowstart=1)

    """ Displays text onto the LCD.
        param: text - the text to display onto the screen
        param: duration - how long to wait after printing the text before exiting the function (seconds)
        param: background - a hex value representing the desired background color
        param: text_color - a hex value representing the desired text color
    """
    def print(self, text: str, duration: int, background: hex, text_color: hex):

        # Make the display context
        splash = displayio.Group()
        self.display.show(splash)

        color_bitmap = displayio.Bitmap(128, 128, 1)    # (making the border)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xffd700 #Gold

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        # Draw a smaller inner rectangle (background)
        inner_bitmap = displayio.Bitmap(108, 108, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = background
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)
        splash.append(inner_sprite)

        # Draw a label
        text_area = label.Label(
                                terminalio.FONT,
                                text=text,
                                color=text_color,
                                anchor_point=(0.5, 1.0),
                                anchored_position=(64,64),
                                scale=2)
        splash.append(text_area)

        time.sleep(duration)


    """ Displays a label on the LCD one letter at a time.
    param: text - the text to display on the LCD
    param: duration - how long to wait after printing the text before exiting the function (seconds)
    param: background - a hex value representing the desired background color
    param: text_color - a hex value representing the desired text color
    """
    def scroll(self, text: str, duration: int, background: hex, text_color: hex):

        # Make the display context
        splash = displayio.Group()
        self.display.show(splash)

        color_bitmap = displayio.Bitmap(128, 128, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xffd700 #Gold

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(108, 108, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = background
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)
        splash.append(inner_sprite)

        curr_text = ""

        # Display the text onto the display, letter-by-letter
        for letter in text:
            curr_text += letter
            # Redraw the inner rectangle to prevent overlapping words
            inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)
            splash.append(inner_sprite)

            text_area = label.Label(
                                    terminalio.FONT,
                                    text=curr_text,
                                    color=text_color,
                                    anchor_point=(0.5, 1.0),
                                    anchored_position=(64,64),
                                    scale=2)
            splash.append(text_area)
            time.sleep(0.5)

        time.sleep(duration)


    """ Displays an image on the LCD.
        param: image_name - a string of the name/path of the desired image to display
        param: duration - how long to wait after printing the text before exiting the function (seconds)
    """
    def displayImage(self, image_name: str, duration: int):
        display = self.display

        # Open the file (eg /purple.bmp)
        with open(image_name, "rb") as bitmap_file:

            # Setup the file as the bitmap data source
            bitmap = displayio.OnDiskBitmap(bitmap_file)

            # Create a TileGrid to hold the bitmap
            tile_grid = displayio.TileGrid(
                bitmap,
                pixel_shader=getattr(bitmap, 'pixel_shader', displayio.ColorConverter())
            )

            # Create a Group to hold the TileGrid
            group = displayio.Group()

            # Add the TileGrid to the Group
            group.append(tile_grid)

            # Add the Group to the Display
            display.show(group)

            time.sleep(duration)    # if needed, wait duration seconds before leaving the function

class Matrix_Keypad:

    def __init__(self, row_pins, col_pins, keys):

        if len(keys) != len(row_pins):
            raise RuntimeError("Key name matrix doesn't match # of colums")
        for row in keys:
            if len(row) != len(col_pins):
                raise RuntimeError("Key name matrix doesn't match # of rows")
        self.row_pins = row_pins
        self.col_pins = col_pins
        self.keys = keys

    @property
    def pressed_keys(self):
        """An array containing all detected keys that are pressed from the initalized
        list-of-lists passed in during creation"""
        # make a list of all the keys that are detected
        pressed = []

        # set all pins pins to be inputs w/pullups
        for pin in self.row_pins + self.col_pins:
            pin.direction = Direction.INPUT
            pin.pull = Pull.UP

        for row, row_pin in enumerate(self.row_pins):
            # set one row low at a time
            row_pin.direction = Direction.OUTPUT
            row_pin.value = False
            # check the column pins, which ones are pulled down
            for col, val in enumerate(self.col_pins):
                if not val.value:
                    pressed.append(self.keys[row][col])
            # reset the pin to be an input
            row_pin.direction = Direction.INPUT
            row_pin.pull = Pull.UP
        return pressed

#Reset Function to center Servos
def reset():
    s1 = 120 #center angles for corresponding parts
    s2 = 60
    s3 = 90
    s4 = 90
    my_servo1.angle = s1 # left foot
    my_servo2.angle = s2 # right foot
    my_servo3.angle = s3 # left hip
    my_servo4.angle = s4 # right hip

#Speaker Initialization
spkrenable = digitalio.DigitalInOut(board.A2) #analog pin assigned provides analog input (not used)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True
wave_file = open("laugh.wav", "rb") #music file for individual dances
wave = WaveFile(wave_file) #creates a wave file to pass as paramater to audo.play() function
wave_file3 = open("billie.wav", "rb")#music file for moon walk dance
wave3 = WaveFile(wave_file3) #creates a wave file to pass as parameter to audo.play() function
wave_file4 = open("zelda.wav", "rb")#music file for walk dance
wave4 = WaveFile(wave_file4) #creates a wave file to pass as parameter to audo.play() function
wave_file5 = open("happy.wav", "rb")#music file for happy_feet dance
wave5 = WaveFile(wave_file5) #creates a wave file to pass as parameter to audo.play() function
wave_file6 = open("drive.wav", "rb")#music file for rhino dance
wave6 = WaveFile(wave_file6) #creates a wave file to pass as parameter to audo.play() function
wave_file7 = open("sax.wav", "rb")#music file for foot_swivel dance
wave7 = WaveFile(wave_file7) #creates a wave file to pass as parameter to audo.play() function
wave_file2 = open("crazy.wav", "rb")#music file for dance routine featuring all dances
wave2 = WaveFile(wave_file2) #creates a wave file to pass as paramater to audo.play() function
audio = AudioOut(board.A0) #analog pin assigned to receive true analog output (connects to speaker)


#Keypad Initialization
cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D7, board.D5)]
rows = [digitalio.DigitalInOut(x) for x in (board.D13, board.D12, board.D11, board.D10)]
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))
keypad = Matrix_Keypad(rows, cols, keys)

#Servo Initialization
pwm1 = pwmio.PWMOut(board.SCL, duty_cycle=2 ** 15, frequency=50) #pwm objects created
pwm2 = pwmio.PWMOut(board.SDA, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm4 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
my_servo1 = servo.Servo(pwm1) #left foot
my_servo2 = servo.Servo(pwm2) #right foot
my_servo3 = servo.Servo(pwm3) #left hip
my_servo4 = servo.Servo(pwm4) #right hip

#LED Initialization
numpix = 16 #the number of LEDs on the neopixel ring
pixpin = board.A1 #the pwm input assignment (receives signals to control LEDs)
strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.15) #assign strip as the LED object

#LCD initialization
lcd = LCD() #creates and LCD() object as defined in the LCD imported file

#Main Code
while True:
    keys = keypad.pressed_keys #holds the value of the pressed key

    if keys == [1]: #if the key pressed is one, execute the first dance
        lcd.print("Dance #1", 0.5, 0x0, 0xFFFFFF) #prints on a black bg with white txt
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.scroll("J. Jacks", 0.5, 0xFFFFFF, 0x154734) #scroll prints on white bg with dark green txt
        lcd.displayImage("jumping_jacks.bmp", 0.1) #displays associated photo on LCD for 0.1s
        audio.play(wave) #plays the individual dance audio
        while audio.playing: #while audio playing execute following
            reset() #reset function
            JUMPING_JACK.jumping_jack(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            #dance function passed the number of LEDs, LED object and servo pwm objects.

    time.sleep(0.1)

    if keys == [2]:
        lcd.print("Dance #2", 0.5, 0x0, 0xFFFFFF) #prints on a black bg with white text
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.scroll("H. Feet", 0.5, 0xFFFFFF, 0x00008B) #scroll prints on white bg with obsidian txt
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.displayImage("happy_feet.bmp", 0.1) #displays associated photo on LCD for 0.1s
        audio.play(wave5) #plays the individual dance audio
        while audio.playing: #while audio playing execute following
            reset() #reset function
            HAPPY_FEET.happy_feet(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            #dance function passed the number of LEDs, LED object and servo pwm objects.
    time.sleep(0.1)

    if keys == [4]:
        lcd.print("Dance #3", 0.5, 0x0, 0xFFFFFF) #prints on a black bg with white text
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.scroll("Walk", 0.5, 0xFFFFFF, 0xFF8C00) #scroll prints on white bg with orange txt
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.displayImage("walk.bmp", 0.1) #displays associated photo on LCD for 0.1s
        audio.play(wave4) #plays the individual dance audio
        while audio.playing: #while audio playing execute following
            reset() #reset function
            WALK.walk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            #dance function passed the number of LEDs, LED object and servo pwm objects.
    time.sleep(0.1)

    if keys == [5]:
        lcd.print("Dance #4", 0.5, 0x0, 0xFFFFFF) #prints on a black bg with white text
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.scroll("F.Swivel", 0.5, 0xFFFFFF, 0x654321) #scroll prints on white bg with dark brown txt
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.displayImage("foot_swivel.bmp", 0.1) #displays associated photo on LCD for 0.1s
        audio.play(wave7) #plays the individual dance audio
        while audio.playing: #while audio playing execute following
            reset() #reset function
            FOOT_SWIVEL.foot_swivel(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            #dance function passed the number of LEDs, LED object and servo pwm objects.
    time.sleep(0.1)

    if keys == [7]:
        lcd.print("Dance #5", 0.5, 0x0, 0xFFFFFF) #prints on a black bg with white text
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.scroll("Rhino", 0.5, 0xFFFFFF, 0x445055) #scroll prints on white bg with grey txt
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.displayImage("rhino.bmp", 0.1) #displays associated photo on LCD for 0.1s
        audio.play(wave6) #plays the individual dance audio
        while audio.playing: #while audio playing execute following
            reset() #reset function
            RHINO.rhino(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            #dance function passed the number of LEDs, LED object and servo pwm objects.

    time.sleep(0.1)

    if keys == [8]:
        lcd.print("Dance #6", 0.5, 0x0, 0xFFFFFF) #prints on a black bg with white text
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.scroll("M. Walk", 0.5, 0xFFFFFF, 0x8B0000) #scroll prints on white bg with dark red txt
        #parameters as defined in LCD imported file (text, duration, bg color, text color)
        lcd.displayImage("moon_walk.bmp", 0.1) #displays associated photo on LCD for 0.1s
        audio.play(wave3) #plays the individual dance audio
        while audio.playing: #while audio playing execute following
            reset() #reset function
            MOONWALK.moonwalk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            #dance function passed the number of LEDs, LED object and servo pwm objects.
    time.sleep(0.1)

    if keys == ['*']:
        reset() #reset function
        print("reset")
    time.sleep(0.1)

    #sequential execution of all dances to create a unique routine
    if keys == [0]:
        audio.play(wave2) #play dance routine audio file
        while audio.playing: #while audio playing execute the following
            #dance functions passed the number of LEDs, LED object and servo pwm objects.
            #reset functions between calls to ensure consistent/safe movements
            #displays associated photos for each dance on LCD for 0.1s
            reset()
            lcd.displayImage("jumping_jacks.bmp", 0.1)
            JUMPING_JACK.jumping_jack(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            JUMPING_JACK.jumping_jack(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            JUMPING_JACK.jumping_jack(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            lcd.displayImage("happy_feet.bmp", 0.1)
            HAPPY_FEET.happy_feet(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            HAPPY_FEET.happy_feet(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            lcd.displayImage("walk.bmp", 0.1)
            WALK.walk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset
            lcd.displayImage("foot_swivel.bmp", 0.1)
            FOOT_SWIVEL.foot_swivel(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            FOOT_SWIVEL.foot_swivel(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            FOOT_SWIVEL.foot_swivel(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            lcd.displayImage("rhino.bmp", 1) #one second display to correct timing
            RHINO.rhino(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            RHINO.rhino(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            lcd.displayImage("moon_walk.bmp", 1.5) #one point five second display to correct timing
            MOONWALK.moonwalk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
            MOONWALK.moonwalk(numpix, strip, my_servo1, my_servo2, my_servo3, my_servo4)
            reset()
    time.sleep(0.1)

