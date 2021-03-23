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

def left_slide(row):
  left_part =  left_collapse(move_to_left(row));
  right_part  = zero_pad_lst(row , left_part);
  return left_part + right_part;
  
def move_to_left(row):
  left_part  = [e for e in row if e != 0 ];
  right_part  = zero_pad_lst(row , left_part);
  return left_part + right_part;
​
def left_collapse(row ):
  if (len(row) < 2 ):
    return row ;
  if (row[0] == row[1]):
    return [row[0]*2] + left_collapse(row[2:]);
  else :
    return [row[0]] + left_collapse(row[1:])
  
def zero_pad_lst(lst , other):
  return [0 for _ in range(0 , len(lst) - len(other))];

