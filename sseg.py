"""Seven Segment Display Driver for esp8266"""

from machine import Pin

__author__ = "Umut Karcı"
__email__ = "cediddi@gmail.com"
__license__ = "MIT"
__version__ = "1.0"


def generate_pins(a, b, c, d, e, f, g, h=None):
    """
    Generates and initializes output pins
    Defaults are: (13,15,0,4,5,12,14,None)
    """
    rval = {
        "a": Pin(a, Pin.OUT),
        "b": Pin(b, Pin.OUT),
        "c": Pin(c, Pin.OUT),
        "d": Pin(d, Pin.OUT),
        "e": Pin(e, Pin.OUT),
        "f": Pin(f, Pin.OUT),
        "g": Pin(g, Pin.OUT),
    }
    if h is not None:
        rval["h"] = Pin(h, Pin.OUT)
    return rval


class SevenSegment:
    """SevenSegment is a helper class for running a single 7segment display"""
    _PATTERNS = [
        "abcdef",
        "bc",
        "abdeg",
        "abcdg",
        "bcfg",
        "acdfg",
        "acdefg",
        "abc",
        "abcdefg",
        "abcdfg"
    ]

    def __init__(self, pins, reverse_polarity=False):
        self._light = not reverse_polarity
        self.pins = pins

    def clear(self):
        """Clears the display"""
        [p.value(not self._light) for p in self.pins.values()]

    def show(self, num):
        """Displays a digit"""
        assert 0 <= num <= 9
        numpattern = self._PATTERNS[num]
        self.clear()
        for pos in numpattern:
            self.pins[pos].value(self._light)


print("'sseg' LOADED")

