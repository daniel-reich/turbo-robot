"""


Write a function that finds the sum of the first `n` natural numbers. **Make
your function recursive.**

###  Examples

    sum_numbers(5) ➞ 15
    # 1 + 2 + 3 + 4 + 5 = 15
    
    sum_numbers(1) ➞ 1
    
    sum_numbers(12) ➞ 78

### Notes

  * Assume the input number is always positive.
  * Check the **Resources** tab for info on recursion.

"""

import sys
sys.setrecursionlimit(3000)
def sum_numbers(n):
  if n==0: return 0
  else: return n+sum_numbers(n-1)

