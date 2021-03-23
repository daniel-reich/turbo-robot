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
    # ax + 1 = b + x
    # ax - x = b - 1
    # x(a - 1) = b - 1
    # x = (b - 1) / (a - 1)
    if a==1 and b==1:
        return 'Any number'
    else:
        try:
            return round((b - 1) / (a - 1), 3)
        except:
            return 'No solution'

