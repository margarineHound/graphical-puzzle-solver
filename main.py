#!/usr/bin/env python3
import tile
from puzzle import puzzle
from square import *
def main():

    # TODO: Definine each tile as a line in a CSV file, where each column is associated with one edge (0th column: top edge, 1st column: right edge, etc.)

    # TODO: Define a function in square.py which accepts a file handle and returns a list of tiles.
    delt = [['a', 'b', 'c', 'd'], ['b','c', 'd', 'a'], ['c', 'd', 'a', 'b'], ['d', 'a', 'b', 'c'], ['a', 'b', 'c', 'd'], ['b','c', 'd', 'a'], ['c', 'd', 'a', 'b'], ['d', 'a', 'b', 'c'], ['d', 'a', 'b', 'c']]
    effect = tile_const(delt) # delt and effect are confusing names. Haha, pick not-confusing ones.

    check(effect) # See TODO above this function declaration. I'm thinking we can omit this.

    ver = puzzle(effect) # ver sounds like "verify" when this is actually a Puzzle instance. It would be better to call this "puz" or similar.

    # The below is kind of what we want
    if ver.verify():
        print("Hell yes!")
    else:
        print("Fuck me... Trying another orientation of tiles...")

if __name__ == "__main__": main()