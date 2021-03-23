"""


 **Stalactites** hang from the ceiling of a cave while **stalagmites** grow
from the floor.

Create a function that determines whether the input represents `"stalactites"`
or `"stalagmites"`. If it represents both, return `"both"`. Input will be a 2D
list, with `1` representing a piece of rock, and `0` representing air space.

### Examples

    mineral_formation([
      [0, 1, 0, 1],
      [0, 1, 0, 1],
      [0, 0, 0, 1],
      [0, 0, 0, 0]
    ]) ➞ "stalactites"
    
    mineral_formation([
      [0, 0, 0, 0],
      [0, 1, 0, 1],
      [0, 1, 1, 1],
      [0, 1, 1, 1]
    ]) ➞ "stalagmites"
    
    mineral_formation([
      [1, 0, 1, 0],
      [1, 1, 0, 1],
      [0, 1, 1, 1],
      [0, 1, 1, 1]
    ]) ➞ "both"

### Notes

  * There won't be any examples where both stalactites and stalagmites meet (because those are called pillars).
  * There won't be any example of neither stalactites or stalagmites.

"""

def mineral_formation(cave):
  
  Stalactites = 0
  Stalagmites = 0
  
  Column = 0
  
  Rows = len(cave)
  Columns = len(cave[0])
  
  while (Column < Columns):
    
    if (cave[0][Column] == 1) and (cave[-1][Column] == 1):
      Stalactites += 1
      Stalagmites += 1
      Column += 1
      
    elif (cave[0][Column] == 0) and (cave[-1][Column] == 1):
      Stalagmites += 1
      Column += 1
      
    elif (cave[0][Column] == 1) and (cave[-1][Column] == 0):
      Stalactites += 1
      Column += 1
    
    else:
      Column += 1
  
  if (Stalactites > 0) and (Stalagmites > 0):
    return "both"
  elif (Stalactites > 0) and (Stalagmites == 0):
    return "stalactites"
  elif (Stalactites == 0) and (Stalagmites > 0):
    return "stalagmites"
  else:
    return "neither"

