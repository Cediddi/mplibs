"""Morse Code Helper for esp8266"""

from time import sleep


class Morse:
    """
    Morse is a helper class for generating and displaying morse code
    takes a Pin object and by default high on that pin means light, unless you set reverse_polarity to true.
    """
    CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
            'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',

            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..',
            '9': '----.'
            }

    def __init__(self, pin, reverse_polarity=False):
        self.pin = pin
        self._light = not reverse_polarity

    def get_morse(self, s):
        """Takes a string and returns a morse code"""
        news = []
        s = s.replace(" ", "/")
        for c in s:
            if c == "/":
                news.append("/")
            else:
                news.append(self.CODE.get(c.upper(), ""))
        return " ".join(news)

    def signal_morse(self, s):
        """Takes a morse code and signals via led"""
        self.pin.value(not self._light)
        for c in s:
            sleep(0.1)
            if c == ".":
                self.pin.value(self._light)
                sleep(0.3)
                self.pin.value(not self._light)
            elif c == "-":
                self.pin.value(self._light)
                sleep(1)
                self.pin.value(not self._light)
            elif c == " ":
                sleep(0.5)
            elif c == "/":
                sleep(0.9)
