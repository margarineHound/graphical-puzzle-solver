#!/usr/bin/env python3

# Refer to https://www.python.org/dev/peps/pep-0008/#class-names
#
# Tile class defines a primitive of the Puzzle class. In the puzzle game, a tile is one of 9 objects that needs to be rotated and placed within a 3x3 grid when attempting to solve the puzzle.
class Tile(object):
    """
    A Tile object embeds a list of edges in the following order:
    [0,1,2,3] => [top, right, bottom, left]
    """
    def __init__(self, edges):
        self.edges = edges # self.edges[0] -> top, self.edges[1] -> right, etc.
    
    """
    rotate performs a virtual rotation on a Tile instance
    top -> right, right -> bottom, bottom -> left, left -> top
    """
    # See https://repl.it/repls/LumberingColdLegacysystem
    # I haven't tested this version which acts on the list property of the class
    def rotate(self, n):
        if n > 0:
            if n > 1:
                return self.rotate(n-1)
            last = self.edges.pop(-1)
            self.edges.insert(0,last)

    def get_top(self):
        """ returns the 1st element in the object"""
        return self._top
    def get_right(self):
        """ returns the 2nd element in the object"""
        return self._right

    def get_bottom(self):
        """ returns the 3rd element in the object"""
        return self._bottom

    def get_left(self):
        """ returns the last element in the object"""
        return self._left



    def __str__(self):
        """ prints a visual representation of each edge for the tile"""

        return f"""---{self._top}----
            |      |
            {self._left}  1  {self._right}
            |      |
            ---{self._bottom}---"""
