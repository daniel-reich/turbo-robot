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

import itertools
​
def concat(*args):
    return list(itertools.chain(*args))

