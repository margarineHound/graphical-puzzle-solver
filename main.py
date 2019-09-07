#!/usr/bin/env python3
from tile import Tile
from puzzle import *
from square import *
import csv

def main():

    try:
        fh = open('tiles.csv', newline='') # file handle
    except OSError as e:
        print(f"File {e.filename} could not be opened")

    tile_list = csvparser(fh)
    tiles = tile_const(tile_list)

    puz = Puzzle(tiles)
    check(puz)

    # The below is kind of what we want
    if puz.verify():
        print("Hell yes!")
    else:
        print("Fuck me... Trying another orientation of tiles...")

if __name__ == "__main__": main()