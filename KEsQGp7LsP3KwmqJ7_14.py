"""


Given a list of distinct integers, create a function that checks if the list
is sorted and rotated **clockwise**. If so, return `"YES"`; otherwise return
`"NO"`.

### Examples

    check([3, 4, 5, 1, 2]) ➞ "YES"
    # The above list is sorted and rotated.
    # Sorted list: [1, 2, 3, 4, 5].
    # Rotating this sorted list clockwise
    # by 3 positions, we get: [3, 4, 5, 1, 2].
    
    check([1, 2, 3]) ➞ "NO"
    # The above list is sorted but not rotated.
    
    check([7, 9, 11, 12, 5]) ➞ "YES"
    # The above list is sorted and rotated.
    # Sorted list: [5, 7, 9, 11, 12].
    # Rotating this sorted list clockwise
    # by 4 positions, we get: [7, 9, 11, 12, 5].

### Notes

N/A

"""

from collections import deque
def check(l):
  t = deque(sorted(l))
  if list(t)==l: return 'NO'
  for i in range(len(l)):
    t.rotate(-1)
    if list(t)==l: return 'YES'
  return 'NO'

