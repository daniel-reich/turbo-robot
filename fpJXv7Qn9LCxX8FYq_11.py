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

import re
​
​
def solve(eq):
    pattern = re.compile(r'.\d+')
    num1 = pattern.findall(eq)
    signal = eq[2]
    if signal == '+':
        return int(num1[1]) - int(num1[0])
    else:
        return int(num1[1]) + int(num1[0])

