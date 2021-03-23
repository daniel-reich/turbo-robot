"""


Given an index using INTEGER division and a list, return the value of the list
with the given index.

### Examples

    value_at([1, 2, 3, 4, 5, 6], 10 // 2) ➞ 6
    
    value_at([1, 2, 3, 4, 5, 6], 8.0 // 2) ➞ 5
    
    value_at([1, 2, 3, 4], 6.535355314 // 2) ➞ 4

### Notes

N/A

"""

def value_at(lst, index):
  return lst[int(index)]

