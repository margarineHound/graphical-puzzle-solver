#!/usr/bin/env python3
import tile
import puzzle
from square import *
def main():

    delt = [['a', 'b', 'c', 'd'], ['b','c', 'd', 'a'], ['c', 'd', 'a', 'b'], ['d', 'a', 'b', 'c'], ['a', 'b', 'c', 'd'], ['b','c', 'd', 'a'], ['c', 'd', 'a', 'b'], ['d', 'a', 'b', 'c'], ['d', 'a', 'b', 'c']]


    effect = tile_const(delt)

    check(effect)

    ver = puzzle(effect)
    print(ver.verify())
    print(ver)

if __name__ == "__main__": main()