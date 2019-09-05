#!/usr/bin/env python3
from tile import tile

# TODO: I'm not sure what this function does, actually. Document its behavior for me so I can determine what we should do with it.
def check(square):
    rotate_n = 0
    # new_list = []
    for item in square:
        top = item.get_top()
        if top is 'b':
            rotate_n = 1
        elif top is 'c':
            rotate_n = 2
        elif top is 'd':
            rotate_n = 3
        else: continue

        if rotate_n != 0:
            item.rotate(rotate_n)

def tile_const(square):
    assert isinstance(square, list), "Not a list"
    if len(square) != 9:
        raise TypeError('tile_const() takes a list of exactly 9 elements')
    tiles = [tile(item) for item in square]
    return tiles
