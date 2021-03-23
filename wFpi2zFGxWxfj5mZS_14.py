"""


Create a function which returns the number of `True` values in a list.

### Examples

    count_true([True, False, False, True, False]) ➞ 2
    
    count_true([False, False, False, False]) ➞ 0
    
    count_true([]) ➞ 0

### Notes

  * Return `0` if given an empty list.
  * All list items are of the type bool (`True` or `False`).

"""

def count_true(lst):
  if lst == list():
    return 0
  else:
    return lst.count(True)

