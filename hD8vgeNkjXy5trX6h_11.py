"""


Create a function that returns all **combinations of size n** from a list.
Sort the list in ascending lexicographical order.

### Examples

    combo([1, 2, 3, 4], 1) ➞ [[1], [2], [3], [4]]
    
    combo([1, 2, 3, 4], 2) ➞ [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    
    combo([1, 2, 3, 4], 5) ➞ []
    
    combo([1, 2, 3, 4], 0) ➞ [[]]

### Notes

  * Lexicographical order: Compare the first element: `[1, 2]` will be before `[2, 4]`. If both share the same first element, compare the second element: `[1, 2]` is before `[1, 3]`, etc.
  * Return an empty list `[]` if `n` exceeds the length of the list.
  * Return `[[]]` if `n` is `0` (see example #4). (Since there is only one combination of length 0: an empty list).

"""

import itertools
def combo(lst, n):
  return [list(x) for x in itertools.combinations(lst, n)]

