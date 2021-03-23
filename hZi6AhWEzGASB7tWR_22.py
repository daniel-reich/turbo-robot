"""


Write a function that takes a list and determines whether it's strictly
increasing, strictly decreasing, or neither.

### Examples

    check([1, 2, 3]) ➞ "increasing"
    
    check([3, 2, 1]) ➞ "decreasing"
    
    check([1, 2, 1]) ➞ "neither"
    
    check([1, 1, 2]) ➞ "neither"

### Notes

  * The last example does NOT count as strictly increasing, since 1-indexed `1` is not strictly greater than the 0-indexed `1`.
  * Input lists have a minimum length of 2.

"""

def check(lst):
    if incr(lst):
        return 'increasing'
    if incr(lst[::-1]):
        return 'decreasing'
    return 'neither'
​
def incr(x):
    for i in range(len(x)-1):
        if x[i] >= x[i+1]:
            return False
    return True

