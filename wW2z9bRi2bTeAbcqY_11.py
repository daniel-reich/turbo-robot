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
  
  ##############################
  # ALGEBRAIC SHUFFLING
  ##############################
  # ax+1    =   b+x
  # ax      =   b+x-1
  # ax      =   (b-1) + x
  # ax - x  =   (b-1)
  # (a-1)x  =   (b-1)
  # ...therefore
  # x = (b-1) / (a-1)
  
  Test_A = a - 1
  Test_B = b - 1
  
  if (Test_B == 0):
    return "Any number"
  elif (Test_A == 0):
    return "No solution"
  else:
    return round(Test_B / Test_A,3)

