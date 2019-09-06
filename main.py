#!/usr/bin/env python3
from tile import Tile
import puzzle
from square import *
import csv

def main():

    try:
        csv_file = open('csvfile.csv', newline='')
    except OSError as e:
        print(f"File {e.filename} could not be opened")

    tile_list = csvparser(csv_file)
    tiles = tile_const(tile_list)

    grid_const = puzzle.Puzzle(tiles)
    check(grid_const) # See TODO above this function declaration. I'm thinking we can omit this.

    # ver = Puzzle(grid_const) # ver sounds like "verify" when this is actually a Puzzle instance. It would be better to call this "puz" or similar.

    # The below is kind of what we want
    if grid_const.verify():
        print("Hell yes!")
    else:
        print("Fuck me... Trying another orientation of tiles...")

if __name__ == "__main__": main()