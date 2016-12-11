from dht import DHT22
from time import sleep

from mplibs.wemos import *

dht_conn = DHT22(Pin(D4))


def measure_realtime():
    dht.measure()
    sleep(0.2)
    dht.measure()
