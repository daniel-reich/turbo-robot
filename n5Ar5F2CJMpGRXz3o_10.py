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
  if 1 in cave[0] and 1 in cave[-1]:
    return "both"
  elif 1 in cave[0]:
    return "stalactites"
  else:
    return "stalagmites"

