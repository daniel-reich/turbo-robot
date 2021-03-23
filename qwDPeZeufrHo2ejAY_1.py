"""


Given a _string_ containing an _algebraic equation_ , calculate and **return
the value of x**. You'll only be given equations for simple **addition** and
**subtraction**.

### Examples

    eval_algebra("2 + x = 19") ➞ 17
    
    eval_algebra("4 - x = 1") ➞ 3
    
    eval_algebra("23 + 1 = x") ➞ 24

### Notes

  * There are spaces between every number and symbol in the string.
  * x may be a negative number.

"""

import re
​
def eval_algebra(s):
    s = s.replace(' ', '').replace('=', '==')
    a, b = map(int, re.findall(r'-? ?\d+', s))
    if eval(s.replace('x', str(a-b))):
        return a - b
    elif eval(s.replace('x', str(b-a))):
        return b - a
    return a + b

