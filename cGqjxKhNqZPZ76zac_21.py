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

from string import ascii_uppercase as asc
​
def fire(matrix, coordinates):
  x, y = asc.index(coordinates[0]), int(coordinates[1]) - 1
  return 'splash' if matrix[x][y] == '.' else 'BOOM'

