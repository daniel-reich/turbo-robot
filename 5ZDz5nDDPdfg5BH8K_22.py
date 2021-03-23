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
    if math.sqrt(n) == 3 or n % 5 == 0:
        return True
    else:
        n2 = 3
        while n2 < n:
            n2 *= 3
        n2 /= 3
​
        for _ in range(int(n2 / 3)):
            n3 = n2
            while n3 < n:
                n3 += 5
                if n3 == n:
                    return True
            n2 /= 3
            if n2 == 1:
                n2 = 0
​
        return False

