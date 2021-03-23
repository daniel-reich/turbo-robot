"""


Create a function that returns the value of x (the "unknown" in the equation).
Each equation will be formatted like this:

    x + 6 = 12

### Examples

    solve("x + 43 = 50") ➞ 7
    
    solve("x - 9 = 10") ➞ 19
    
    solve("x + 300 = 100") ➞ -200

### Notes

  * " **x** " will always be in the same place (you will _not_ find an equation like **_6 + x = 12_** ).
  * Every equation will include either subtraction ( **-** ) or addition ( **+** ).
  * " **x** " may be negative.

"""

def solve(eq):
  x = eq.split(" ")
  if "+" in x:
    return int(x[4]) - int(x[2])
  else:
    return int(x[4]) + int(x[2])

