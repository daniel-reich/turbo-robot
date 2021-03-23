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
  try:
    if a == 2 and b == 2:
      return 'Any number'
    return round((b - 3*a + 4) / (a - b),3)
  except:
    return 'No solution'

