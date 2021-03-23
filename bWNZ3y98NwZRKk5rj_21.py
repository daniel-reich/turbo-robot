"""


Create a function that returns a number which can block the player from
reaching 3 in a row in a game of Tic Tac Toe. The number given as an argument
will correspond to a grid of Tic Tac Toe: topleft is 0, topright is 2,
bottomleft is 6, and bottomright is 8.

  * Create a function that takes two numbers `a`, `b` and returns another number.
  * This number should be the final one in a line to block the player from winning.

### Examples

    block_player(0, 3) ➞ 6
    
    block_player(0, 4) ➞ 8
    
    block_player(3, 5) ➞ 4

### Notes

The values given will always have two filled squares in a line.

"""

def block_player(a, b):
  
  Lowest = min(a,b)
  Highest = max(a,b)
  
  # Lowest as Top Left (0)
  
  if (Lowest == 0) and (Highest == 1):
    return 2
  elif (Lowest == 0) and (Highest == 2):
    return 2
  elif (Lowest == 0) and (Highest == 3):
    return 6
  elif (Lowest == 0) and (Highest == 4):
    return 8
  elif (Lowest == 0) and (Highest == 6):
    return 3
  elif (Lowest == 0) and (Highest == 8):
    return 4
  
  # Lowest as Top Middle (1)
  
  elif (Lowest == 1) and (Highest == 2):
    return 0
  elif (Lowest == 1) and (Highest == 4):
    return 7
  elif (Lowest == 1) and (Highest == 7):
    return 4
  
  # Lowest as Top Right (2)
  
  elif (Lowest == 2) and (Highest == 4):
    return 6
  elif (Lowest == 2) and (Highest == 5):
    return 8
  elif (Lowest == 2) and (Highest == 6):
    return 4
  elif (Lowest == 2) and (Highest == 8):
    return 5
  
  # Lowest as Left Middle (3)
  
  elif (Lowest == 3) and (Highest == 4):
    return 5
  elif (Lowest == 3) and (Highest == 5):
    return 4
  elif (Lowest == 3) and (Highest == 6):
    return 0
  
  # Lowest as Middle (4)
  
  elif (Lowest == 4) and (Highest == 5):
    return 3
  
  elif (Lowest == 4) and (Highest == 6):
    return 2
  
  elif (Lowest == 4) and (Highest == 7):
    return 1
  
  elif (Lowest == 4) and (Highest == 8):
    return 0
  
  # Lowest as Right Middle (5)
  
  elif (Lowest == 5) and (Highest == 8):
    return 2
  
  # Lowest as Bottom Left (6)
  
  elif (Lowest == 6) and (Highest == 7):
    return 8
  
  # Lowest as Bottom Middle (7)
  
  elif (Lowest == 7) and (Highest == 8):
    return 6
  
  # Just in case...
  
  else:
    return "Who knows?"

