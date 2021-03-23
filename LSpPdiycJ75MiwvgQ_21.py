"""


How many ways are there to navigate through a grid `(w * h)`?

![Grid](https://edabit-challenges.s3.amazonaws.com/grid_paths.png)

Suppose you're on a 4 × 6 grid, and want to go from the bottom left to the top
right. How many different paths can you take? Avoid backtracking, you can only
move right or up.

Create a function that takes `w`idth and `h`eight and returns the amount of
possibilities.

### Examples

    grid_pos([1, 1]) ➞ 2
    
    grid_pos([6, 4]) ➞ 210
    
    grid_pos([5, 5]) ➞ 252

### Notes

Check the **Resources** tab for a detailed explanation.

"""

def grid_pos(lst):
  f = lst[0] + lst[1]
  fact = 1
  for i in range(1,lst[1]+1):
    fact *= i
  i = f
  fact2 = 1
  while True:
    if i > lst[0]:
      fact2 *= i
    else:
      break
    i -= 1
  return round(fact2 / fact)

