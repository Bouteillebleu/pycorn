#
# Copyright 2008 Torne Wuff
#
# This file is part of Pycorn.
#
# Pycorn is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#

import _metalmem

_sizes = (
        False,
        (_metalmem.peek8, _metalmem.poke8, (-0x80, 0xff)),
        (_metalmem.peek16, _metalmem.poke16, (-0x8000, 0xffff)),
        False,
        (_metalmem.peek32, _metalmem.poke32, (-0x80000000, 0xffffffff))
        )

def reader(bytes):
    return _sizes[bytes][0]

def writer(bytes):
    return _sizes[bytes][1]

def checkaddr(address, bytes):
    if address < 0 or address > 0xffffffffL:
        raise ValueError('address must be between 0 and 0xFFFFFFFF')
    if bytes < 1 or bytes > 4 or bytes == 3:
        raise ValueError('bytes must be 1, 2 or 4')
    if address % bytes != 0:
        raise ValueError('address must be aligned to a multiple of bytes')

def checkvalue(bytes, value):
    lo = _sizes[bytes][2][0]
    hi = _sizes[bytes][2][1]
    if value < lo or value > hi:
        raise ValueError('value must be between %s and %s' % (lo, hi))

def peek(address, bytes=4):
    checkaddr(address, bytes)
    return _sizes[bytes][0](address)

def poke(address, value, bytes=4):
    checkaddr(address, bytes)
    checkvalue(bytes, value)
    _sizes[bytes][1](address, value)

membuf = _metalmem.membuf
