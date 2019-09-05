#!/usr/bin/env python3

# Puzzle class defines the structure and behavior of a collection of Tile objects. The state of a Puzzle is not mutated directly. Rather, the state of the Tile objects attached to a Puzzle instance are each mutable, implicitly modifiying the state of the Puzzle object. Thus, all methods of the Puzzle class are read-only.
class Puzzle(object):
    # constructor
    # tiles is a list of tiles
    def __init__(self, tiles):
        self.tiles = tiles

    def verify(self):
        """the verify implementation of the overall
        puzzle"""
        assert isinstance(self.tiles, list)
        assert len(self.tiles) == 9

        flag = True
        for i in self.tiles:
            if i.get_top() != 'a':
                flag = False
            if i.get_right() != 'b':
                flag = False
            if i.get_bottom() != 'c':
                flag = False
            if i.get_left() != 'd':
                flag = False
        return flag

    def __str__(self):
        return f"""
            {str(self.tiles[0])} {str(self.tiles[1])} {str(self.tiles[2])}
            {str(self.tiles[3])} {str(self.tiles[4])} {str(self.tiles[5])}
            {str(self.tiles[6])} {str(self.tiles[7])} {str(self.tiles[8])}
        """