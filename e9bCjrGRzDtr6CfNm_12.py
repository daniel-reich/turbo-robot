"""


Consider the equation `ax-b=bx-3a+4` where `a` and `b` are constants. Create a
function that takes numbers `a` and `b` as arguments, and returns the solution
of the equation.

  * If the equation does not have a solution, return `"No solution"`.
  * If any number satisfies the equation, return `"Any number"`.

### Examples

    solve(1, 2) ➞ -3.0
    
    solve(-4, -6) ➞ 5.0
    
    solve(4, 1) ➞ -2.333

### Notes

Round your answer to three decimal places.

"""

def solve(a, b):
  left_side, right_side = a - b, 4 + b - (3 * a)
​
  if not left_side and not right_side:
    return "Any number"
  elif not left_side and right_side:
    return "No solution"
  else:
    return round(right_side / left_side, 3)

