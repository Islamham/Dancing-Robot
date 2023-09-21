view image of robot: [imgur.com/a/7JM7JYP](https://imgur.com/a/7JM7JYP)

# **Dance Robot: Overview**

**1. The six dance moves:**

**jumpingJack:**  
The robot performs a compulsory dynamic stretch known as the jumping jack to warm up before heading out to the dance floor.

**happy_feet:**  
Following tik tok trends, our robot performs a delightful and uplifting dance called the happy feet (or heel to toe) by swinging its feet in a groovy/stylish manner.

**walk:**  
Sometimes a simple groovy/stylish walk is all you need to liven up the dance floor. Given the lack of knees, it may appear more like a waddle at times.

**foot_swivel:**  
The robot shows you the funk attainable by just a single foot and a little creativity.

**rhino:**  
Just like a rhino or bull paws the ground before a charge, the robot paws its one foot before immediately discharging a ferocious tackle.

**moonwalk:**  
Inspired by the great Michael Jackson, the robot performs a sideways rendition of the famous “moonwalk” dance.

**2. What info the LCD displays**
The LCD, essentially, displays either text or an image at any given time. Before each dance runs, the LCD displays the text “Dance #x”, with x being the number of the dance (1-6). Then it displays, letter by letter (using a scroll function), the name of the dance, as per the names listed above. The display uses variations of a golden border with either a black or white background, complemented by contrasting text colors. As the dance begins, the LCD shows an image chosen to represent the respective dance and maintains that image throughout the duration of the dance performance. 

# **Implementation Details**

## **1. Imports and Libraries**
In `demo.py`, corresponding to the `code.py` file on the ItsyBitsy, numerous libraries are imported. These include:
- Dance moves files
- Speaker libraries
- Neopixel libraries
- Matrix keypad libraries
- Servo motor libraries
- TFT LCD libraries

Additional libraries support core functionalities, such as `digitalIO` and `board`.

## **2. Dance Implementation and Features**
Each dance file houses a class with a dance move function. This function encompasses both the dance move and an associated light show via Neopixel LED rings. Initialization for all features, including the TFT LCD and servos, is in the `demo.py` file. The program uses the keypad for input, determining the mode of operation, with individual dances triggered by specific keys, a sequence of dances triggered by another, and a reset function.

## **3. Servo Motor Implementation**
From the `adafruit_motor` library, servos are initialized via PWM output objects. Four pins from the ItsyBitsy M4 Express are dedicated to the SG92R servo motors. Each motor is responsible for specific movements, with set centered angles and directional movements based on angle adjustments. Care is taken to avoid hazardous angles that could cause the robot to collapse or the feet to collide.

## **4. TFT LCD Software Implementation**
Key Libraries and their functions:
- `board`: Connects the microcontroller to the LCD.
- `terminalio`: Manages the font of the displayed text.
- `displayio`: Regulates what is showcased on the LCD.
- `adafruit_display_text.label`: Creates text labels for display.
- `ST7735R`: Initializes the display.

Within `tftlcd.py`, an LCD class is created to control the LCD in the main demo code. The constructor initializes the display and assigns the appropriate pins. Three primary functions exist:
- `print`: Centralizes text on the screen with specified background and text colors.
- `scroll`: Similar to `print`, but reveals text letter by letter.
- `displayImage`: Showcases an image for a designated duration.

The display construction employs `displayio.Group()` as a canvas, creating visual elements using `Bitmap`, `TileGrid`, and `Label`. Each function has meticulous designs to ensure correct and appealing visual display.

## **5. Neopixel LED Ring Implementation**
Using the `neopixel` library, an LED object is created, enabling the utilization of `fill()` and `write()` functions. The patterns and dances displayed on the LED ring are crafted using individual LED assignments or the `fill()` method:
- **foot_swivel**: A mix of `fill()` for initial red display and individual assignments for the spiraling pattern of red and blue.
- **happy_feet**: Looping use of `fill()` to cycle through rainbow colors on all LEDs.
- **jumpingJack**: Individual LED assignments create a rainbow spiral as LEDs light up in sequence and opposites go off.
- **moonwalk**: A spiraling pattern of white and red, followed by flashes of red and white.
- **Rhino**: Uses a yellow spiral pattern, which once complete, employs the `fill()` method to flash red and white across all LEDs.
- **walk**: Uses `fill()` to show a consistent color across all LEDs, without looping, initiating at the start of every dance move.

## **6. Matrix Keypad Implementation**
The Keypad, with its matrix connectivity, is mirrored in the code with a matrix-style structure. Assigned keys, consistent with keypad button numbers, represent each cell's value. The keypad carries out the designated code chunk when the input matches an assigned key's values. A continuous loop using the `keys` variable as a condition ensures execution. Remember, button values correspond to their row and column positioning. For instance, the button intersection of D5 row and D11 column corresponds to button 1.

## **7. Speaker Implementation**
Libraries from `audiocore` and `audioio` aid the speaker's functioning. The `audiocore` library offers the `WaveFile()` function, and `audioio` supplies the `AudioOut()` function. `digitalio` facilitates the creation of a speaker enable object through an analog pin assignment. During initialization, a local .wav file is opened, converted using `WaveFile()`, and then dispatched to `audio.play()` whenever sound output is necessary. These calls occur right before initiating a dance function. Concurrent execution is ensured by placing dance functions within a "while `audio.playing`" loop. The `AudioOut()` function transmits genuine analog audio output to its assigned pin (`board.A0`). Notably, even though `board.A2` is designated to the speaker enable object, it's not employed since no input is required. Furthermore, the .wav files used were initially converted from 32-bit 48000 Hz stereo to 16-bit 8000 Hz mono using the "Audacity" software.
