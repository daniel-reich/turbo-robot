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

def only_5_and_3(n):
  return only_5_and_3_util(0, 0, n)
​
def only_5_and_3_util(current_number, increment, n):
    if increment == 3 and current_number > 0:
        current_number *= increment
    else:
        current_number += increment
    if current_number < n:
        for i in range(3, 6, 2):
            if only_5_and_3_util(current_number, i, n):
                return True
        return False
    elif current_number > n:
        return False
    else:
        return True

