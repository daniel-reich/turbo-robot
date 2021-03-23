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
    if n % 3 == 0:
        m = n//3
        m2 = n - 5
    else:
        m = n - 5
        m2 = None
    if m == 5 or m == 3 or m2 == 5 or m2 == 3:
        return True
    elif m > 1:
        if m2 is not None:
            return only_5_and_3(m) or only_5_and_3(m2)
        else:
            return only_5_and_3(m)
    else:
        return False

