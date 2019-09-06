#!/usr/bin/env python3

class Puzzle(object):
    """
    Puzzle class defines the structure and behavior of a collection of Tile objects. The state of a Puzzle is not mutated directly. Rather, the state of the Tile objects attached to a Puzzle instance are each mutable, implicitly modifiying the state of the Puzzle object. Thus, all methods of the Puzzle class are read-only.
    """


    def __init__(self, tiles):
        """
        constructor
        tiles is a list of tiles
        """

        self.tiles = tiles
        assert isinstance(self.tiles, list)
        assert len(self.tiles) == 9


    def verify(self):
        " verify returns a boolean that"

        #left and middle column comparisons
        if self.tiles[0].edges[1] != self.tiles[1].edges[3]:
            return False

        if self.tiles[3].edges[1] != self.tiles[4].edges[3]:
            return False

        if self.tiles[6].edges[1] != self.tiles[7].edges[3]:
            return False

        #right and middle column comparisons
        if self.tiles[2].edges[3] != self.tiles[1].edges[1]:
            return False

        if self.tiles[5].edges[3] != self.tiles[4].edges[1]:
            return False

        if self.tiles[8].edges[3] != self.tiles[7].edges[1]:
            return False

        #upper and middle row comparisons
        if self.tiles[0].edges[2] != self.tiles[3].edges[0]:
            return False

        if self.tiles[1].edges[2] != self.tiles[4].edges[0]:
            return False

        if self.tiles[2].edges[2] != self.tiles[5].edges[0]:
            return False

        #middle and lower row comparisons
        if self.tiles[3].edges[2] != self.tiles[6].edges[0]:
            return False

        if self.tiles[4].edges[2] != self.tiles[7].edges[0]:
            return False

        if self.tiles[5].edges[2] != self.tiles[8].edges[0]:
            return False

        else:
            return True


    # and __repr__!
    def __str__(self):
        return f"""
            {str(self.tiles[0])} {str(self.tiles[1])} {str(self.tiles[2])}
            {str(self.tiles[3])} {str(self.tiles[4])} {str(self.tiles[5])}
            {str(self.tiles[6])} {str(self.tiles[7])} {str(self.tiles[8])}
        """