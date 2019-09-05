#!/usr/bin/env python3

# Puzzle class defines the structure and behavior of a collection of Tile objects. The state of a Puzzle is not mutated directly. Rather, the state of the Tile objects attached to a Puzzle instance are each mutable, implicitly modifiying the state of the Puzzle object. Thus, all methods of the Puzzle class are read-only.
class Puzzle(object):
    # constructor
    # tiles is a list of tiles
    def __init__(self, tiles):
        self.tiles = tiles

    # verify returns a boolean that 
    def verify(self):
        # TODO: We can remove these. We are the only users of this application. Sanitation on input for projects that only have 1 or 2 developers and which is not coupled to a production database/sensitive information is not necessary. It's good that you're thinking about this, but it's not necessary. In fact, if you want sanitation like this, it's better to place it in the constructor, so that you have guarantees when it comes time to calling methods. I recommend removing these assertions, but if you'd like to keep them then let's move this logic to the constructor.
        assert isinstance(self.tiles, list)
        assert len(self.tiles) == 9

        # What you've written isn't quite what we want. Note that you should be comparing the values of adjacent edges to each other, not the values of edges to constant values (like 'a' or 'b'...). We should be doing something similar to the following (shitty pseudo-code):
        # if self.tiles[0][right-side] != self.tiles[1][left-side]:
        #     return false
        #   NOTE
            # self.tiles[0] -> bottom left tile (matrix indices: [3,1])
            # self.tiles[1] -> bottom middle tile (matrix indices: [3,2])
        # if self.tiles[1][right-side] != self.tiles[2][left-side]:
        #     return false
        # ..... (there will be 12 of these if statements, one for each inner edge pair)
        # .....
        # if self.tiles[7][right-side] !=  self.tiles[8][left-side]:
        #   return false     
        # else:
        #   return true

            if i.get_top() != 'a':
                flag = False
            if i.get_right() != 'b':
                flag = False
            if i.get_bottom() != 'c':
                flag = False
            if i.get_left() != 'd':
                flag = False
        return flag

    # Ah, it's __str__!! Right! Good job!
    def __str__(self):
        return f"""
            {str(self.tiles[0])} {str(self.tiles[1])} {str(self.tiles[2])}
            {str(self.tiles[3])} {str(self.tiles[4])} {str(self.tiles[5])}
            {str(self.tiles[6])} {str(self.tiles[7])} {str(self.tiles[8])}
        """