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

    #TODO: UPDATE: In response to your questions, I have some questions of my own:
    # 1.) How many unique solutions can a puzzle have? is there only one unique solution?
	That's a great question. I'm not sure how to prove how many exist without solving for all of them. Maybe 0, maybe n, haha.
    # 2.) Are we, at this stage, concerned with the level of efficiency with which the solution needs to be discovered?
	Not. at. all. haha. Once we have a good solution I'll port it over to Go and I'll show you how we can speed up our solution by at least 10x.
    # 3.) Do you have a recommended algorithm, and/or know of any algorithms that might deal with this? I suppose this deals directly with my first question, since if there true exists only one unique solution, then we might be dealing with as many as 9! permutations for just the tile placements, not accounting for tile rotations.
	I have an algorithm, but it's from my brain (it's not a published/known one that you can read about elsewhere). It's as simple as laying down the puzzle in some "zero" state and then rotating the tiles, one by one, and moving the tiles, one by one, until there's a solution, working our way through something like the  9!4! placements and rotations...
    # 4.) Dealing with your last point is easy, obviously, though the path forward needs to be discussed before progressing any further, imo
	Let's do it. I'm down to chat this weekend.
	

    def centerCheck(tcenter, tdyn, epos1, epos2=None):
        falseCenter = False
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
        count = 0
        while tstatic.edges[epos1] != tdyn.edges[epos2]:
                tdyn.rotate(1)
                count += 1

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
