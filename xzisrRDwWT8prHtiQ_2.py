"""


Create a function that takes an array of integers and returns all pairs of
integers that have a **difference of two**. The resulting array should be
sorted in **ascending order** of values.

### Examples

    difference_two([1, 2, 3, 4]) ➞ [[1, 3], [2, 4]]
    
    difference_two([1, 23, 3, 4, 7]) ➞ [[1, 3]]
    
    difference_two([4, 3, 1, 5, 6]) ➞ [[1, 3], [3, 5], [4, 6]]

### Notes

Assume there are no duplicate integers in the array. The order of the integers
in the input array should not matter.

"""

def difference_two(lst):
  return sorted([[i,i+2] for i in lst if i+2 in lst])

