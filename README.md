@@ -0,0 +1,46 @@
# square_rotator

<img src="./puzzle.jpg" width="500"/>

## Problem Description

This project attempts to solve the popular 3x3 square puzzle game.

The objective of this puzzle is to place and rotate 9 individual "tile"s within a 3x3 grid such that each edge shared by two tiles in the grid are "aligned" with respect to each other. To aid in visualizing this puzzle we have included an image file (`puzzle.jpg`) in the root of this repository.

Each tile is a square where on each edge is contained half of a picture (we'll call this a demi-picture). The demi-picture on a given edge has no relationship to any other edge on that tile; that is, that same demi-image may appear on another edge or on no other edge on that tile at all.

The goal is to place each tile in the 3x3 grid in some orientation that ensures that all of the paired edges between tiles match. Considering the attached puzzle, many of the edges have already been paired. The top left tile and its southern neighbor form a matching pair. Likewise, the bottom left tile and its northern neighbor form a matching pair. But, note that either (or both) the upper left tile and its eastern neighbor are improperly positioned and oriented such that their edges don't form a matching pair. Its unclear which (if either or both tiles) changes need to be repositioned - placed in a different spot on the 3x3 grid - and/or reoriented - rotated in place. Discounting rotations of the entire puzzle and repeated demi-images , there are something like 4!9! (~8 million) possible combinations of tile placements and their individual orientations.

There may be more than one solution. The goal is simply to find one, and to do it in a reasonable amount of time. I have it on good account that a dullard sitting at a table trying to solve this puzzle might waste oh, I don't know, as much as 20 hours trying to solve this by hand. A computer should be able to do this much faster.

## Test Case

The file containing a description of each tile (`tiles.csv`) corresponds exactly to the example puzzle image (`puzzle.jpg`) included in this project repository.

Each row of the `.csv` corresponds to a tile, with the tiles being indexed left to right and then top to bottom.

The column of each `.csv` describes the edges of each tile, as determined by the picture. There are a set of 4 images in the puzzle, so a set of 8 demi-images.

1. A star (S)
1. A ringed planet (R)
1. An earth-like planet (E)
1. A striped, Mars-like planet (M)

For each of these images we required a sub-label to associated an edge of a tile with a particular demi-image. This can be done arbitrarily. So, we begin by trying to label the first tile's edges (top, right, bottom, left):

1. R:- (the minus flavor/kind of the ringed planet)
1. S:- (the minus flavor of the star)
1. R:- (the minus flavor of the ringed planet is the same as the "bottom" half)
1. S:+ (the plus flavor of the star)

Note that the ringed planet only comes in one flavor. The top and bottom halfs are the same and always match, no matter what. This will need to be considered separately.

Considering the second tile's edges (top, right, bottom, left):

1. M:- (the minus flavor of the Mars-like planet)
1. M:+ (the plus flavor of the Mars-like planet)
1. E:- (the minus flavor of the Earth-like planet)
1. R:- (the minus flavor of the ringed planet)

Note that the value of every edge up until this point has been arbitrary except for the ringed planet edges and those of the Mars-like planet. The ringed planet has been discussed already. The Mars-like planet is the kind of case we are really interested in. Tile 2 has both demi-images of the Mars-like planet. Thus, the the choice of labelling the first demi-image as "bottom" or "top" was arbitrary. However, the labelleling of the right edge containing the other demi-image is constrained by the labelling of the first. These two demi-images, when they share an edge, will form a match. When all of the tiles' edges match their neighbors' edges then the puzzle is solved. The rest of the edges are labelled in `tiles.csv`.