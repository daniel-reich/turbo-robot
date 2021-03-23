"""


Given a list, rotates the values clockwise by one (the last value is sent to
the first position).

Check the examples for a better understanding.

### Examples

    rotate_by_one([1, 2, 3, 4, 5]) ➞ [5, 1, 2, 3, 4]
    
    rotate_by_one([6, 5, 8, 9, 7]) ➞ [7, 6, 5, 8, 9]
    
    rotate_by_one([20, 15, 26, 8, 4]) ➞ [4, 20, 15, 26, 8]

### Notes

All lists are the same size, so it's not necessary to use loops or to think
much about complex solutions.

"""

def rotate_by_one(arr):
  first_elem = arr.pop(-1)
  arr2 = list(arr)
  arr2.insert(0,first_elem)
  return arr2

