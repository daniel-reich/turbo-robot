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
    pos = {'A':0,'B':1,'C':2,'D':3,'E':4}
    y = pos[coordinates[0]]
    x = int(coordinates[1])-1
    if matrix[y][x] == "*":
        return "BOOM"
    return "splash"

