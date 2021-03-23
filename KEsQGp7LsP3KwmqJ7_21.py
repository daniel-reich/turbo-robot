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

def check(lst):
  arr = sorted(lst)
  for i in range(len(lst)):
    arr.append(arr[0])
    arr.pop(0)
    if lst == arr and arr != sorted(lst):
      return "YES"
  return "NO"

