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

def solve(a,b):
    if a == 1 and b == 1:
        return "Any number"
    else:
        try:
            first = a - 1
            second = -1 + b
            third = round(second / first,3)
            return third
        except ZeroDivisionError:
            return "No solution"

