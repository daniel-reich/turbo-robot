"""


 **2048** is a game where you need to slide numbered tiles (natural powers of
2) up, down, left or right on a square grid to combine them in a tile with the
number 2048.

The sliding procedure is described by the following rules:

  * Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid.
  * If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided.
    * If more than one variant of merging is possible, move direction shows one that will take effect.
  * Tile cannot merge with another tile more than one time.

Sliding is done almost the same for each direction and for each row/column of
the grid, so your task is to implement only the left slide for a single row.

### Examples

    left_slide([2, 2, 2, 0]) ➞ [4, 2, 0, 0]
    # Merge left-most tiles first.
    
    left_slide([2, 2, 4, 4, 8, 8]) ➞ [4, 8, 16, 0, 0, 0]
    # Only merge once.
    
    left_slide([0, 2, 0, 2, 4]) ➞ [4, 4, 0, 0, 0]
    
    left_slide([0, 2, 2, 8, 8, 8]) ➞ [4, 16, 8, 0, 0, 0]

### Notes

  * Input row can be of any size (empty too).
  * Input row will contain only natural powers of 2 and 0 for empty tiles.
  * Keep trailing zeros in the output.

"""

def left_slide(tiles):
    '''
    Returns tiles after they have been merged to the left as per the rules of
    2048 described in the instructions.
    '''
    active_tiles = [tile for tile in tiles if tile]  # remove spaces
    merged_tiles = []
    
    i = 0
    size = len(active_tiles)
    while i < size:
        if i == size - 1:
            merged_tiles.append(active_tiles[i])  # last tile unchanged
            break
        if active_tiles[i] == active_tiles[i+1]:
            merged_tiles.append(active_tiles[i] * 2)  # merge the tiles
            i+= 2  # skip over next tile
        else:
            merged_tiles.append(active_tiles[i])
            i+= 1
        
    return merged_tiles + [0] * (len(tiles) - len(merged_tiles)) # 0 fill at right

