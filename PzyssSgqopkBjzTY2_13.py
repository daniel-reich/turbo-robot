"""


A maze can be represented by a 2D matrix, where `0`s represent **walkeable**
areas, and `1`s represent walls. You start on the upper left corner and the
exit is on the most lower right cell.

Create a function that returns `true` if you can walk from one end of the maze
to the other. You can only move up, down, left and right. You **cannot move
diagonally**.

### Examples

    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 0, 0, 1],
      [1, 1, 1, 1, 1, 0, 0]
    ]) ➞ true
    
    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 0, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 0, 1, 0, 0, 1],
      [1, 1, 0, 0, 1, 1, 1]
    ]) ➞ false
    
    # This maze only has dead ends!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1]
    ]) ➞ false
    
    # Exit only one block away, but unreachable!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 0]
    ]) ➞ true

### Notes

  * In a maze of size `m x n`, you enter at `[0, 0]` and exit at `[m-1, n-1]`.
  * There can be dead ends in a maze - one exit path is sufficient.

"""

def can_exit(lst):
  width = len( lst[ 0 ] )
  heigth = len( lst )
  paths = [ [ [ 0, 0 ] ] ]
  while True :
    new_paths = [ ]
    for p in paths :
      x, y = p[ -1 ][ 0 ], p[ -1 ][ 1 ]
      if lst[ max( 0, y - 1 ) ][ x ] == 0 and [ x, max( 0, y - 1 ) ] not in p :
        new_paths.append( p + [ [ x, max( 0, y - 1 ) ] ] )
      if lst[ y ][ min( width - 1, x + 1 ) ] == 0 and [ min( width - 1, x + 1 ), y ] not in p :
        new_paths.append( p + [ [ min( width - 1, x + 1 ), y ] ] )
      if lst[ min( heigth - 1, y + 1 ) ][ x ] == 0 and [ x, min( heigth - 1, y + 1 ) ] not in p :
        new_paths.append( p + [ [ x, min( heigth - 1, y + 1 ) ] ] )
      if lst[ y ][ max( 0, x - 1 ) ] == 0 and [ max( 0, x - 1 ), y ] not in p :
        new_paths.append( p + [ [ max( 0, x - 1 ), y ] ] )
    if len( new_paths ) == 0 :
      return False
    for p in new_paths :
      if [ width - 1, heigth - 1 ] in p :
        return True
    paths = new_paths

