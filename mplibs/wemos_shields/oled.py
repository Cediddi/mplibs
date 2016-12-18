from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

from mplibs.helpers import chunk
from mplibs.wemos import *

i2c = I2C(Pin(SCL), Pin(SDA))
oled_conn = SSD1306_I2C(64, 48, i2c)


def ez_text(fb):
    oled_conn.fill(0)
    if type(fb) != str:
        fb = chunk(fb[:48], 8)
    for text, row in zip(fb, range(0, 48, 8)):
        oled_conn.text("{:8.8}".format(str(text)), 0, row)
    oled_conn.show()
