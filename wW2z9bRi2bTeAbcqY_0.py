"""


Consider the equation `ax+1=b+x` where `a` and `b` are constants. Create a
function that takes numbers `a` and `b` as arguments, and returns the solution
of the equation.

  * If the equation does not have a solution, return `"No solution"`.
  * If any number satisfies the equation, return `"Any number"`.

### Examples

    solve(4, 7) ➞ 2.0
    
    solve(9, 5) ➞ 0.5
    
    solve(12, -4) ➞ -0.455

### Notes

Round your answer to three decimal places.

"""

def solve(a, b):
  return "Any number" if (1 - b) == 0 else "No solution" if (1 - a) == 0 else round((1 - b)/(1 - a),3)

