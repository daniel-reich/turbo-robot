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
  pass_next = False
  frames = []
  result = 0
  for i in pins:
    if pass_next:
      frames[-1].append(i)
      pass_next = False
    else:
      if i != 10:
        pass_next = True
      frames.append([i])
  for i in range(10):
    if frames[i][0] == 10:
      result += 10
      if len(frames[i+1]) == 2:
        result += sum(frames[i+1])
      else: 
        result += frames[i+1][0] + frames[i+2][0]
    elif sum(frames[i]) == 10:
      result += 10
      result += frames[i+1][0]
    else:
      result += sum(frames[i])
  return result

