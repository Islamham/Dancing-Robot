
import board
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

import time

""" This class makes an LCD object, which demo.py uses to control the TFT LCD. """
class LCD:
    def __init__(self):
        displayio.release_displays()    # release any resources that may be in use on the LCD currently
        
        # set up pins 
        self.spi = board.SPI()      # use .SPI() to read the SPI pins connected to microcontroller
        self.tft_cs = board.A4      # cs is connected to A4
        self.tft_dc = board.A3      # dc connected to A3
        self.reset = board.A5       # reset connected to A5

        # make the bisplay bus (set to four wire)
        self.display_bus = displayio.FourWire(
            self.spi, command=self.tft_dc, chip_select=self.tft_cs, reset=self.reset
        )
        
        # initialize the display using the display bus
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
        self.display.show(splash)       # show what is currently on splash

        color_bitmap = displayio.Bitmap(128, 128, 1)    # (making the border)
        color_palette = displayio.Palette(1)            # we will use a color palette of 1 color for the border
        color_palette[0] = 0xffd700 #Gold

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)      # make a sprite out of the above bitmap 
        splash.append(bg_sprite)    # put the sprite on the display

        # Draw a smaller inner rectangle (background)
        inner_bitmap = displayio.Bitmap(108, 108, 1)    
        inner_palette = displayio.Palette(1)        # using a color palette of 1 color for background
        inner_palette[0] = background               # use the color specified by the user
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)     # make a sprite for the background
        splash.append(inner_sprite)     # put the sprite on the display

        # Draw a label
        text_area = label.Label(
                                terminalio.FONT,    # use the normal terminal font
                                text=text,          # the text is specified by user
                                color=text_color,   # text color specified by user
                                anchor_point=(0.5, 1.0),    # anchor point for the text is bottom center of the text
                                anchored_position=(64,64),      # the text will be in the center of the screen
                                scale=2)                # make the text bigger than normal
        splash.append(text_area)    # put the label on the display

        time.sleep(duration)         # sleep for a specified extra amount of time

    
    """ Displays a label on the LCD one letter at a time.
    param: text - the text to display on the LCD
    param: duration - how long to wait after printing the text before exiting the function (seconds)
    param: background - a hex value representing the desired background color
    param: text_color - a hex value representing the desired text color
    """
    def scroll(self, text: str, duration: int, background: hex, text_color: hex):

        # Make the display context
        splash = displayio.Group()
        self.display.show(splash)        # show what is currently on splash

        color_bitmap = displayio.Bitmap(128, 128, 1)        # (making the border)
        color_palette = displayio.Palette(1)               # we will use a color palette of 1 color for the border
        color_palette[0] = 0xffd700 #Gold

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)        # make a sprite out of the above bitmap 
        splash.append(bg_sprite)          # put the sprite on the display

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(108, 108, 1)                  
        inner_palette = displayio.Palette(1)          # using a color palette of 1 color for background
        inner_palette[0] = background            # use the color specified by the user
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)          # make a sprite for the background
        splash.append(inner_sprite)           # put the sprite on the display

        curr_text = ""           # initialize the text to be displayed as an empty string

        # Display the text onto the display, letter-by-letter
        for letter in text:
            curr_text += letter           # one letter is added to the string which will be displayed
            # Redraw the inner rectangle to prevent overlapping words
            inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)
            splash.append(inner_sprite)

            text_area = label.Label(
                                terminalio.FONT,    # use the normal terminal font
                                text=text,          # the text is specified by user
                                color=text_color,   # text color specified by user
                                anchor_point=(0.5, 1.0),    # anchor point for the text is bottom center of the text
                                anchored_position=(64,64),      # the text will be in the center of the screen
                                scale=2)                # make the text bigger than normal
            splash.append(text_area)        # put the label on the screen
            time.sleep(0.5)         # sleep for 0.5 seconds before putting the next letter on the screen

        time.sleep(duration)         # sleep for a specified extra amount of time


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


