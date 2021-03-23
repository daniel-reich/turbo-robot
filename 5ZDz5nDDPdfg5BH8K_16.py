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
​
def only_5_and_3(n):
  if n % 5 == 0:
    return True
  else:
    threes = list(map(lambda x: pow(3,x),range(1,math.ceil(math.log(n,3)))))
    fives = list(map(lambda x: n - x,threes))
    lst = list(filter(lambda x: x % 5 == 0,fives))
    return len(lst) > 0

