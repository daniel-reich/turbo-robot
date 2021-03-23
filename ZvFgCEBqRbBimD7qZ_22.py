"""


Tenpin bowling scores can range from 0 (all gutter balls) to 300 (a perfect
game). If you are unfamiliar with scorekeeping, please see the **Resource**
for a quick description.

A complete record of a 10 frame bowling game can be given as a list of the
number of pins knocked down by each ball in sequence from beginning to the end
of the game.

Create a function whose argument is such a list. The function should return
the final score.

### Examples

    bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) ➞ 300
    
    bowling([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) ➞ 80
    
    bowling([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) ➞ 150
    
    bowling([10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]) ➞ 200

### Notes

The number of balls thrown for a complete game can vary from 11 to 21
depending on the number of strikes thrown.

"""

def bowling(pins, b=-1, f=1, sp=0, st=0):
  if not pins:
    return 0
​
  p = pins[0]
  s = p * (1 + sp + st)
  sp, st = st, 0
​
  if f == 10:
    return s + bowling(pins[1:], -1, f, sp, st)
  if b != -1:
    return s + bowling(pins[1:], -1, f + 1, sp + (b + p == 10), st)
  if p == 10:
    return s + bowling(pins[1:], -1, f + 1, sp, st + 1)
  return s + bowling(pins[1:], p, f, sp, st)

