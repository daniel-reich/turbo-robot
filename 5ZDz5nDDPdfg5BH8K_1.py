"""


Starting with either `3` or `5` and given these operations:

  * add `5`
  * multiply by `3`

You should say if it is possible to reach the target number `n`.

### Examples

    only_5_and_3(14) ➞ True
    # 14 = 3*3 + 5
    
    only_5_and_3(25) ➞ True
    # 25 = 5+5+5+5+5
    
    only_5_and_3(7) ➞ False
    # There exists no path to the target number 7

### Notes

You can solve this problem by recursion or algebra.

"""

import math
def only5and3(n):
  if math.log(n,3)%1 == 0 or n%5 == 0:
    return True
  else:
    n -= 5
    if 3 < n < 5 or n < 3:
      return False
    return only5and3(n)

