import time
import digitalio
import board
# import adafruit_matrixkeypad
from digitalio import Direction, Pull
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


cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D7, board.D5)]
rows = [digitalio.DigitalInOut(x) for x in (board.D13, board.D12, board.D11, board.D10)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = Matrix_Keypad(rows, cols, keys)

while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
    time.sleep(0.1)