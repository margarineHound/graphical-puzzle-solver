#!/usr/bin/env python3

#tile.py
class tile(object):
    """
    Creates a tile, specifying the edges in the following order:
    top -> right -> bottom -> left
    """
    def __init__(self, edges):
        if isinstance(edges, list) and len(edges) == 4:
            self._top = edges[0]
            self._right = edges[1]
            self._bottom = edges[2]
            self._left = edges[3]
            self._tile = [self._top, self._right, self._bottom, self._left]

    def rotate(self, n):
        """rotate the tile"""

        for i in range(n):
            self._tile.insert(0, self._tile.pop())

            self._top = self._tile[0]
            self._right = self._tile[1]
            self._bottom = self._tile[2]
            self._left = self._tile[3]

    def get_top(self):
        """ returns the 1st element in the object"""
        return self._top
    def get_right(self):
        """ returns the 2nd element in the object"""
        return self._right

    def get_bottom(self):
        """ returns the 3rd element in the object"""
        return self._top

    def get_left(self):
        """ returns the last element in the object"""
        return self._top



    def __str__(self):
        """ prints a visual representation of each edge for the tile"""

        return f"""
            ---{self._top}----
            |      |
            {self._left}  1  {self._right}
            |      |
            ---{self._bottom}---
        """
