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
  
  CODE = "ABCDE"
  Target = str(coordinates)
  
  First = str(Target[0])
  Second = str(Target[1])
  
  Row = CODE.index(First)
  Column = int(Second) - 1
  
  Outcome = matrix[Row][Column]
  
  if (Outcome == "."):
    return "splash"
  elif (Outcome == "*"):
    return "BOOM"
  else:
    return "I don't know!"

