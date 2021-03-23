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
  shot = 1
  score = 0
  frame = 1
  frame_score = [0]*10
  for pin in range(len(pins)):
    score += pins[pin]
    frame_score[frame-1] += pins[pin]
    if shot == 1:
      if pins[pin] < 10:
        shot = 2
      elif pins[pin] == 10:
        if frame < 10:
          score += pins[pin+1] + pins[pin+2]
          frame_score[frame-1] += pins[pin+1] + pins[pin+2]
        else:
          score += sum(pins[pin+1::])
          frame_score[frame-1] += sum(pins[pin+1::])
          break
        frame+=1
    elif shot == 2:
      shot = 1
      if pins[pin] + pins[pin-1] == 10:
        if frame < 10:
          score += pins[pin+1]
          frame_score[frame-1] += pins[pin+1]
        else:
          score += sum(pins[pin+1::])
          frame_score[frame-1] += sum(pins[pin+1::])
          break
      frame += 1
  return score

