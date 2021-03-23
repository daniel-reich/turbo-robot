"""


Write a function that returns the greatest common divisor of all list
elements. If the greatest common divisor is `1`, return `1`.

### Examples

    GCD([10, 20, 40]) ➞ 10
    
    GCD([1, 2, 3, 100]) ➞ 1
    
    GCD([1024, 192, 2048, 512]) ➞ 64

### Notes

  * List elements are always greater than `0`.
  * There is a minimum of two list elements given.

"""

def GCD(lst):
    state = True
    if min(lst) > 1:
        for i in range(min(lst), 1, -1):
            for j in lst:
                if j % i != 0:
                    state = False
            if state:
                return i
            else:
                state = True
        return 1
    else:
        return 1

