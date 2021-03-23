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

def bowling(pins):
  frames = [0]*10
  i = 0
  pins = pins + [0]*(24-len(pins))
​
  for frame in range(10):
    frames[frame] += pins[i] + pins[i+1]
    if pins[i] == 10: # strike
      frames[frame] += pins[i+2]
    elif (pins[i] + pins[i+1]) == 10: # spare
      frames[frame] += pins[i+2]
      i += 1
    else:
      i += 1
    i += 1
    
  return sum(frames)

