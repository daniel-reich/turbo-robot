"""


Create a function that takes an integer `n` and returns the **factorial of
factorials**. See below examples for a better understanding:

### Examples

    fact_of_fact(4) ➞ 288
    # 4! * 3! * 2! * 1! = 288
    
    fact_of_fact(5) ➞ 34560
    
    fact_of_fact(6) ➞ 24883200

### Notes

N/A

"""

import math
from functools import reduce
def fact_of_fact(n):
  m = [math.factorial(i) for i in list(range(1, n+1))]
  return reduce((lambda x, y: x * y), m)

