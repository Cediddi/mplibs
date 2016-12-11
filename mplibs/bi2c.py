"""A better I2C class for bulk write operations"""

import machine

from mplibs.helpers import chunk


class I2C(machine.I2C):
    def writeto_mem(self, addr, pos, data, chunksize=8):
        chunks = map(bytearray, chunk(data, chunksize))
        current_pos = pos
        for chk in chunks:
            super().writeto_mem(addr, current_pos, chk)
            current_pos += 8
