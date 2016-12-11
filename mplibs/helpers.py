"""Helpers for mplibs"""


def chunk(iterable, chunk_size):
    """http://stackoverflow.com/a/12797249/2202986"""
    iterable = iter(iterable)
    while True:
        chk = None
        try:
            chk = next(iterable)
            for _ in range(chunk_size-1):
                chk += next(iterable)
            yield chk
        except StopIteration:
            if chk is not None :
                yield chk
            break