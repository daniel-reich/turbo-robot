"""


In **Block Dude** , the main character can climb boxes, but only if they are
stacked in a particular way so that he is able to climb them one at a time.
More specifically, **he can only climb UP or DOWN one box at a time**.

Let `1`s represent the boxes, and `0` represent the background. Write a
function that returns `True` if block dude **can travel from the left side to
the right side of the screen** given his constraints.

For example, the sample layout below should return `True`.

    [
      [0, 0, 0, 0, X, 0, 0, 0, 0],
      [0, 0, 0, X, 1, X, X, 0, 0],
      [0, X, X, 1, 1, 1, 1, X, 0],
      [X, 1, 1, 1, 1, 1, 1, 1, X]
    ]

Since block dude can travel across these boxes (Note: X's are just to show
walking path and are **not** part of the actual input). On the other hand:

    [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0, 0],
      [0, X, X, 1, 1, 1, 1, 0, 0],
      [X, 1, 1, 1, 1, 1, 1, 1, 0]
    ]

Should return `False`, since block dude is stuck at column 3, being unable to
climb 2 boxes at once.

### Examples

    can_traverse([
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 1, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 0]
    ]) ➞ False
    
    # Block dude can't jump down 2 blocks.
    
    can_traverse([
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 1],
      [0, 0, 1, 1, 1, 0, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 1]
    ]) ➞ True
    
    # Note: Sometimes the exit is at the top!
    
    can_traverse([
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 0]
    ]) ➞ True
    
    can_traverse([
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 0]
    ]) ➞ False
    
    # Block dude can't climb 2 blocks.

### Notes

Check the **Resources** tab for a link to play block dude.

"""

def can_traverse(x):
  heights = []
  for c in range(len(x[0])):
    height = 0
    for r in range(len(x)):
      if x[r][c] == 1:
        height += 1
    heights.append(height)
  for i in range(len(heights)-1):
    if abs(heights[i] - heights[i+1]) > 1:
      return False
  return True

