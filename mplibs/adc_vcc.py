# https://github.com/micropython/micropython/issues/2352#issuecomment-251020631
# Author: eduvik
# Modified!

import esp
from flashbdev import bdev
import machine


def set_adc_mode(vcc=True):
    mode = enable * 255  # A small hack
    sector_size = bdev.SEC_SIZE
    flash_size = esp.flash_size()  # device dependent
    init_sector = int(flash_size / sector_size - 4)
    data = bytearray(esp.flash_read(init_sector * sector_size, sector_size))
    if data[107] == mode:
        return  # flash is already correct; nothing to do
    else:
        data[107] = mode  # re-write flash
        esp.flash_erase(init_sector)
        esp.flash_write(init_sector * sector_size, data)
        print("ADC mode changed in flash; restart to use it!")
        return
