"""Seven Segment Display Driver for esp8266"""

from machine import Pin


class SevenSegment:
    """SevenSegment is a helper class for running a single 7segment display"""
    _PATTERNS = [
        0b11111100,
        0b01100000,
        0b11011010,
        0b11110010,
        0b01100110,
        0b10110110,
        0b10111110,
        0b11100000,
        0b11111110,
        0b11110110,
    ]

    @staticmethod
    def generate_pins(a, b, c, d, e, f, g, h=None):
        """
        Generates and initializes pins for seven segment, takes 8 integers a to g. h is optional.
        """
        rval = [
            Pin(a, Pin.OUT)
            Pin(b, Pin.OUT)
            Pin(c, Pin.OUT)
            Pin(d, Pin.OUT)
            Pin(e, Pin.OUT)
            Pin(f, Pin.OUT)
            Pin(g, Pin.OUT)
        ]
        if h is not None:
            rval.append(Pin(h, Pin.OUT))
        return rval

    def __init__(self, pins, reverse_polarity=False):
        self._light = not reverse_polarity
        if type(pins[0]) == int:
            pins = self.generate_pins(*pins)
        self.pins = pins

    def clear(self):
        """Clears the display"""
        [p.value(not self._light) for p in self.pins.values()]

    def show(self, num):
        """Displays a digit"""
        assert 0 <= num <= 9
        numpattern = self._PATTERNS[num]
        self.clear()
        for idx, _pin in enumerate(self.pins):
            if numpattern & bit:
                _pin.value(self._light)
            else:
                _pin.value(not self._light)
