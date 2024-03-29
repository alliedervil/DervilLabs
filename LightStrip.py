"""
# LightStrip.py
# Re-implementing the old NeoPixel class into a LightStrip class
# This separates out the single internal state machine so it is not used
# for other composite lights if any
# Also moved to a more capable NeoPixel library by blaz-r
"""

import time, neopixel
from Lights import *

class LightStrip(Light):
    """
    Although technically a composite light, a neopixel is a PIO-driven set of lights
    using a single output pin. So you do not send it composite lights, but just the pin
    it is connected to. It is a composite light because it has multiple lights, but
    they cannot technically be controlled individually.
    """

    FILLS = 0
    CHASES = 1
    RAINBOW = 2

    def __init__(self, pin=22, numleds=16, brightness=0.5):
        """
        Constructor for neopixel will create its own internal statemachine
        Note that if any other state machine is running, this will break the existing
        statemachine. This refers to the Pico PIO statemachine, not any software state
        machines.
        """

        self._pin = pin
        self._numleds = numleds
        self._brightness = brightness
        self._running = False

        # Create the StateMachine with the ws2812 program, outputting on pin
        self._pix = neopixel.Neopixel(numleds, 1, pin, "RGB")
        self._pix.brightness(int(brightness * 255))

    def on(self):
        """ Turn all LEDs ON - all white """

        self._pix.fill(WHITE)
        self._pix.show()
    
    def off(self):
        """ Turn all LEDs OFF - all black """
        self._running = False
        time.sleep(0.1)
        self._pix.clear()
        self._pix.show()

    def setColor(self, color, numPixels= -1):
        """ Turn all LEDs up to a set number of pixels to a specific color """
        if numPixels < 0 or numPixels > len(self._ar):
            numPixels = len(self._ar)
        for i in range(numPixels):
            self._pix.set_pixel(i, color)
        for i in range(numPixels,len(self._ar)):
            self._pix.set_pixel(i, BLACK)
        self._pix.show()

    def setPixel(self, pixelno, color):
        """ Turn a single pixel a specific color """
        self._pix.set_pixel(pixelno, color)
        self._pix.show()

    def setBrightness(self, brightness=0.5):
        """ Change the brightness of the pixel 0-1 range """
        self._brightness = brightness
        self._pix.brightness(int(brightness * 255))

    def run(self, runtype=0):
        """ Run a single cycle of FILLS, CHASES or RAINBOW """
        self._running = True
        if runtype == LightStrip.FILLS:
            print("fills")
            for color in COLORS:
                if not self._running:
                    break       
                self.setColor(color)
                sleep(0.2)
        elif runtype == LightStrip.CHASES:
            print("chases")
            for color in COLORS:
                if not self._running:
                    break       
                self.color_chase(color, 0.01)
        else:
            print("rainbow")
            self.rainbow_cycle(0)
        self._running = False


    ################# Internal functions should not be used outside here #################
    def color_chase(self, color, wait):
        for i in range(self._numleds):
            if not self._running:
                break
            self._pix.set_pixel(i, color)
            time.sleep(wait)
            self._pix.show()
        time.sleep(0.2)
    
    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)
    
    
    def rainbow_cycle(self, wait):
        for j in range(255):
            if not self._running:
                break
            for i in range(self._numleds):
                rc_index = (i * 256 // self._numleds) + j
                self._pix.set_pixel(i, self.wheel(rc_index & 255))
            self._pix.show()
            time.sleep(wait)


# Some color definitions
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
ORANGE = (255, 164, 0)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE, ORANGE)
