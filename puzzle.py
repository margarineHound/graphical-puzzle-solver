#!/usr/bin/env python3

# Puzzle class defines the structure and behavior of a collection of Tile objects. The state of a Puzzle is not mutated directly. Rather, the state of the Tile objects attached to a Puzzle instance are each mutable, implicitly modifiying the state of the Puzzle object. Thus, all methods of the Puzzle class are read-only.
class Puzzle(object):
    """
    verifies the overall picture
    """
    def __init__(self, tile_list):
        self.tile_list = tile_list

    def verify(self):
        """the verify implementation of the overall
        puzzle"""
        assert isinstance(self.tile_list, list)
        assert len(self.tile_list) == 9

        flag = True
        for i in self.tile_list:
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
            {str(self.tile_list[0])} {str(self.tile_list[1])} {str(self.tile_list[2])}
            {str(self.tile_list[3])} {str(self.tile_list[4])} {str(self.tile_list[5])}
            {str(self.tile_list[6])} {str(self.tile_list[7])} {str(self.tile_list[8])}
        """