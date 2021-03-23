"""


Remember the game Battleship? Ships are floating in a matrix. You have to fire
torpedos at their suspected coordinates, to try and hit them.

Create a function that takes a list of lists (matrix) and a coordinate as a
string. If the coordinate contains only water `"."`, return `"splash"` and if
the coordinate contains a ship `"*"`, return `"BOOM"`.

### Examples

    [
      [".", ".", ".", "*", "*"],
      [".", "*", ".", ".", "."],
      [".", "*", ".", ".", "."],
      [".", "*", ".", ".", "."],
      [".", ".", "*", "*", "."],
    ]
    
    fire(matrix, "A1") ➞ "splash"
    
    fire(matrix, "A4") ➞ "BOOM"
    
    fire(matrix, "D2") ➞ "BOOM"

### Notes

  * The provided matrix is always a square.
  * The provided matrix will not be larger than 5 * 5 ( A1 * E5).

"""

def fire(matrix, coordinates):
  coord = coordinates[0]
  y = int(coordinates[1])
  if coord == 'A':
    x = 0
  elif coord == 'B':
    x = 1
  elif coord == 'C':
    x = 2
  elif coord == 'D':
    x = 3
  elif coord == 'E':
    x = 4
  if matrix[x][y-1] == '.': return 'splash'
  else: return 'BOOM'

