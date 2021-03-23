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

def check(start, target):
  if start == target:
    return True
  elif start > target:
    return False
    
  return check(start*3, target) or check(start+5, target)
​
def only_5_and_3(n):
  return check(3, n) or check(5, n)

