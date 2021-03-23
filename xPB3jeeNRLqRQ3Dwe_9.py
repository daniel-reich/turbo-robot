"""


Create a function to find `None` in a list of numbers. The return value should
be the index where `None` is found. If `None` is not found in the list, then
return `-1`.

### Examples

    find_none([1, 2, None]) ➞ 2
    
    find_none([None, 1, 2, 3, 4]) ➞ 0
    
    find_none([0, 1, 2, 3, 4]) ➞ -1

### Notes

`None` will occur in the input list only once.

"""

def find_None(lst):
  if None in lst:
    return lst.index(None)
  else:
    return -1

