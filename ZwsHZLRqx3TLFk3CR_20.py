"""


Create a function that takes a list of factorial expressions and returns the
sum.

### Examples

    eval_factorial(["2!", "3!"]) ➞ 8
    
    eval_factorial(["5!", "4!", "2!"]) ➞ 146
    
    eval_factorial(["0!", "1!"]) ➞ 2

### Notes

0! and 1! both equal 1.

"""

import math
def eval_factorial(lst):
  sum_num = 0
  for num in lst:
    x = int(num.split("!")[0])
    sum_num += math.factorial(x)
  return sum_num

