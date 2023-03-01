#!/usr/bin/python3
def raise_exception():
    x = "123"
    y = 456
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("x and y must be integers")
