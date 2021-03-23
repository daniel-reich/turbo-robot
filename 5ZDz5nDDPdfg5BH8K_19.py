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
    flag = 0
    for i in range(1, n):
        for j in range(n):
            if ((3**i) + (5*j)) == n or 5*j == n:
                return True
                break
    else:
        return False

