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
  stalactite = 0
  stalagmite = 0
  for el in cave[0]:
    if el == 1:
      stalactite = 1
      break
  for el in cave[-1]:
    if el == 1:
      stalagmite = 1
      break
  if (stalactite == 1 and stalagmite == 1):
    return "both"
  elif stalactite == 1:
    return "stalactites"
  else:
    return "stalagmites"

