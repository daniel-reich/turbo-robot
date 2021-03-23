"""


Create a function that takes a list and finds the integer which appears an odd
number of times.

### Examples

    find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
    
    find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
    
    find_odd([10]) ➞ 10

### Notes

There will always only be one integer that appears an odd number of times.

"""

def find_odd(lst):
  ans = 0
  for i in lst:
    ans^=i
  return ans

