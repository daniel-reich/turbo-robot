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
    new = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            new.append('in')
        else:
            new.append('de')
    if len(set(new)) == 2:
        return 'neither'
    elif set(new) == {'in'}:
        return 'increasing'
    else:
        return 'decreasing'

