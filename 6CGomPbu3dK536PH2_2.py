"""
Create a function that takes in a list and returns a list of the accumulating
sum.

### Examples

    accumulating_list([1, 2, 3, 4]) ➞ [1, 3, 6, 10]
    # [1, 3, 6, 10] can be written as  [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]
    
    accumulating_list([1, 5, 7]) ➞ [1, 6, 13]
    
    accumulating_list([1, 0, 1, 0, 1]) ➞ [1, 1, 2, 2, 3]
    
    accumulating_list([]) ➞ []

### Notes

An empty list input `[]` should return an empty list `[]`.

"""

from itertools import accumulate
def accumulating_list(lst):
  return list(accumulate(lst))

