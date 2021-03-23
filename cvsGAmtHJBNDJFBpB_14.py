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
  r = len(x)-1
  c = 0
  while c != len(x[0])-1:
    print(c,r)
    # if on bottom
    if r == len(x)-1:
      if x[r][c+1] == 0: c = c+1
      elif x[r][c+1] == 1 and x[r-1][c+1] == 0: r, c = r - 1, c + 1
      else: break
    # if on next up
    elif r == len(x)-2:
      if x[r+1][c+1] == 0: c, r = c+1, r+1
      elif x[r][c+1] == 1 and x[r-1][c+1] == 0: r, c = r-1, c+1
      elif x[r][c+1] == 0 and x[r+1][c+1] == 1: c += 1
      else: break
    # if on top
    elif r == 0:
      if x[r+1][c+1] == 0 and x[r+2][c+1] == 1: c, r = c+1, r+1
      elif x[r][c+1] == 0 and x[r+1][c+1] == 1: c += 1
      else: break
    # else anywhere else
    else:
      if x[r+1][c+1] == 0 and x[r+2][c+1] == 1: c, r = c+1, r+1
      elif x[r][c+1] == 0 and x[r+1][c+1] == 1: c += 1
      elif x[r][c+1] == 1 and x[r-1][c+1] == 0: r, c = r-1, c+1
      else: break
  if c == len(x[0])-1: return True
  return False

