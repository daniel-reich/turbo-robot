"""


Create a function that returns all sublists in a list that sum to a particular
value. Return the sublists in the following order:

  1. First by **ascending length**.
  2. Second by comparing element-by-element, starting from the leftmost one. Put the list with the **smaller** element first in the pairwise comparison.

The following example will illustrate:

    get_subsets([-3, -2, -1, 0, 1, 2, 3], 2)
    [ # All the subsets below sum to 2.
      [2],
      [-1, 3],
      [0, 2], # Same length: -1 < 0, so [-1, 3] goes before [0, 2]
      [-3, 2, 3],
      [-2, 1, 3],
      [-1, 0, 3],
      [-1, 1, 2],
      [-3, 0, 2, 3],
      [-2, -1, 2, 3],
      [-2, 0, 1, 3], # Same length + same first element: -1 < 0, so [-2, -1, 2, 3] goes before [-2, 0, 1, 3]
      [-1, 0, 1, 2],
      [-3, -1, 1, 2, 3],
      [-2, -1, 0, 2, 3],
      [-3, -1, 0, 1, 2, 3]
    ]

### Examples

    get_subsets([-1, 0, 1, 2], 2) ➞ [[2], [0, 2], [-1, 1, 2], [-1, 0, 1, 2]]
    
    get_subsets([-1, 0, 1, 2], 3) ➞ [[1, 2], [0, 1, 2]]
    
    get_subsets([1, 2, 3, 4], 5) ➞ [[1, 4], [2, 3]]
    
    get_subsets([-1, 0, 1, 2], 4) ➞ []

### Notes

  * Lists will have unique numbers.
  * Return an empty list if there does not a exist a subset whose numbers sum to that value (see fourth example).

"""

import itertools
def get_subsets(lst, n):
  subsets = {}
  for i in range(len(lst)+1):
    subsets[i] = []
  for choice in itertools.product([0,1],repeat=len(lst)):
    subset = [lst[i] for i in range(len(choice)) if choice[i]]
    if sum(subset) == n:
      subsets[len(subset)].append(tuple(subset))
  return [list(t) for v in subsets.values() for t in sorted(v)]

