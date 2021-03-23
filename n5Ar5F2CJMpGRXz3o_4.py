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
 stalac = False
 stalag = False
 for x in cave[0]:
    if x != 0:
           stalac = True
 for x in cave[3]:
  if x != 0:
          stalag = True
 if (stalag and stalac) == True:
   return "both"
 elif stalag == True:
   return "stalagmites"
 elif stalac == True:
   return "stalactites"

