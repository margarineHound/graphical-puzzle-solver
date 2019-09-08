#!/usr/bin/env python3
from puzzle import Puzzle
from tile import Tile
import csv

def csvparser(cfile):
    """takes a csv file, and returns a list of tiles"""

    csvreader = csv.reader(cfile, delimiter = ',')
    tile = []
    count = 0
    for row in csvreader:
        if count == 0:
            count += 1
            continue
        else:
            tile.append(row[1:])
    return tile


def rotate_count(tile_obj, n):
    for i in range(n):
        tile_obj.rotate(n)


def tile_const(grid):
    assert isinstance(grid, list), "Not a list"
    if len(grid) != 9:
        raise TypeError('tile_const() takes a list of exactly 9 elements')
    tiles = [Tile(item) for item in grid]
    return tiles


def check(square):
    """checks if a tile is in the proper orientation.
    If not, rotates the tile by determinig the # of rotations
    and calling the rotate function from the tile class."""
    # assuming a 3x3 grid has 9 ordered elements,# i.e. it is outlined in the
    # following manner:
    #   -------
    #   |A|B|C|
    #   -------
    #   |D|E|F|
    #   -------
    #   |G|H|I|
    #   -------
    # Therefore, we start by matching the center tile with its surrounding tiles
    # and continue thence until all tiles are properly aligned with their surrounding
    # tiles

    # TODO: I have some qusetions - note that I think this is not what we should be doing. I think doing "dumb" rotations and then doing a puzzle.verify() after every operation is a good first start.
    # 1.) Which tile is supposed to be in the center?
    # 2.) Does this change if the tile initially assigned to the center is not "supposed" to be there (there is no solution if that tile is kept in the center position)?
    # 3.) Note that if tcenter.edges[epos1] does not complete any demi-image on any of tdyn's edges that this while loop will never exit.
    def centerCheck(tcenter, tdyn, epos1, epos2=None):
        """checks the edges of the center tile, with those of its immediate
        surrounding tiles """
        if epos2 == None:
            if epos1 == 0:
                epos2 = 2
            elif epos1 == 1:
                epos2 = 3
            elif epos1 == 2:
                epos2 = 0
            elif epos1 == 3:
                epos2 = 1
            else:
                raise Exception('Invalid value for epos1 passed to centerCheck: ', epos1)
        else:
            pass

        while tcenter.edges[epos1] != tdyn.edges[epos2]:
                tdyn.rotate(1)

    # TODO: Note that if tstatic.edges[epos1] does not complete any demi-image on any of tdyn's edges that this while loop will never exit.
    def tileCheck(tstatic, tdyn, epos1, epos2):
        """checks and aligns the matching edges of a given tiles, against
        that of a neighboring tile, provided the overlapping edges are given"""

        while tstatic.edges[epos1] != tdyn.edges[epos2]:
                tdyn.rotate(1)

    tA = square.tiles[0]
    tB = square.tiles[1]
    tC = square.tiles[2]
    tD = square.tiles[3]
    tcent = square.tiles[4]
    tF = square.tiles[5]
    tG = square.tiles[6]
    tH = square.tiles[7]
    tI = square.tiles[8]

    #checks and aligns the center tile against its immediate surrounding edges
    for i in range(len(tcent.edges)):
        tiles = [tB, tD, tF, tH]
        centerCheck(tcent, tiles[i], i)

    #checks and aligns the remaining tiles, against tiles that have already been
    #algined by the previous loop
    tileCheck(tB, tA, 3, 1)
    tileCheck(tB, tC, 1, 3)
    tileCheck(tH, tG, 3, 1)
    tileCheck(tH, tI, 1, 3)