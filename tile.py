#!/usr/bin/env python3

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


    def rotate(self, n):
        if n > 0:
            if n > 1:
                return self.rotate(n-1)
            last = self.edges.pop(-1)
            self.edges.insert(0,last)


    def __str__(self):
        return f"""---{self.edges[0]}----
            |      |
            {self.edges[3]}  1  {self.edges[1]}
            |      |
            ---{self.edges[2]}---"""
