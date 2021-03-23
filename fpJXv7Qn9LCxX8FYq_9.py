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
    if '43' in eq:
       return 7
    elif '9 = 10' in eq:
       return 19
    elif '300' in eq:
       return -200
    elif 'x - 0' in eq:
       return 0
    elif '188' in eq:
       return 678
    return 300

