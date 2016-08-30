"""Helpers for mplibs"""


def chunk(iterable, chunk_size):
    """http://stackoverflow.com/a/12797249/2202986"""
    iterable = iter(iterable)
    while True:
        chk = []
        try:
            for _ in range(chunk_size):
                chk.append(next(iterable))
            yield chk
        except StopIteration:
            if chk:
                yield chk
            break
