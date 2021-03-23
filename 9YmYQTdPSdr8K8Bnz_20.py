"""


Write a function that takes a list and returns a new list with unique positive
(more than 0) numbers.

### Examples

    unique_lst([-5, 1, -7, -5, -2, 3, 3, -5, -1, -1]) ➞ [1, 3]
    
    unique_lst([3, -3, -3, 5, 5, -6, -2, -4, -1, 3]) ➞ [3, 5]
    
    unique_lst([10, 6, -12, 13, 5, 5, 13, 6, 5]) ➞ [10, 6, 13, 5]

### Notes

  * Return the elements in the order that they are found in the list.
  * Your function should also work for empty lists.

"""

def unique_lst(lst):
  return sorted(set(filter(lambda x: x>0,lst)), key=lst.index)

