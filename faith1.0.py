# -*- coding: utf-8 -*-

import os
from random import randint
def readback(fp, pos):
    while pos >= 0:
        fp.seek(pos)
        yield fp.read(1)
        pos -= 1
def readrand(filename):
    size = os.path.getsize(filename)
    offset = randint(0, size - 10)
    with open(filename) as fp:
        for char in readback(fp, offset):
            if char == '\n':
                break
        else:
            fp.seek(0)
        return fp.readline()
print(readrand('fort1.txt'))
