"""


Create a function that takes a list and returns the number of ALL elements
within it (including those within the sub-level list(s)).

### Examples

    deep_count([1, 2, 3]) ➞ 3
    
    deep_count([[1], [2], [3]]) ➞ 6
    
    deep_count(["x", "y", ["z"]]) ➞ 4
    
    deep_count(["a", "b", ["c", "d", ["e"]]]) ➞ 7

### Notes

In the examples above, notice how the sub-lists within the main list count as
an element _as well as_ the elements within that sub-list.

"""

def deep_count(lst):
  counta=0
  for i in lst:
    if (isinstance(i,list)):
      counta+=deep_count(i)
  return len(lst)+counta

