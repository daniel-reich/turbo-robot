"""


Create a function that concatenates **n** input lists, where **n** is
variable.

### Examples

    concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]
    
    concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]
    
    concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]
    
    concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]

### Notes

Lists should be concatenated in order of the arguments.

"""

def concat(*args):
  return [a for arg in args for a in arg]

