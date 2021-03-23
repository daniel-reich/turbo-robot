"""


Create a function that returns the original value from a list with too many
sub-lists.

### Examples

    de_nest([[[[[[[[[[[[3]]]]]]]]]]]]) ➞ 3
    
    de_nest([[[[[[[True]]]]]]]) ➞ True
    
    de_nest([[[[[[[[[[[[[[[[["edabit"]]]]]]]]]]]]]]]]]) ➞ "edabit"

### Notes

You only need to retrieve one element.

"""

def deNest(lst):
  if type(lst[0])!=list: return lst[0]
  return deNest(lst[0])

