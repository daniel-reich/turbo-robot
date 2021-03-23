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
  abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  nums = "1234565789"
​
  for i in abc and coordinates[0]:
    col = abc.find(i)
    for k in nums and coordinates[1]:
      row = nums.find(k)
      if matrix[col][row] == ".":
        return "splash"
      elif matrix[col][row] == "*":
        return "BOOM"
      else:
        return "Something went wrong...."

