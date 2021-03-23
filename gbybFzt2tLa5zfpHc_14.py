"""


Write a function that returns all sets of three elements that sum to 0.

### Examples

    three_sum([0, 1, -1, -1, 2]) ➞ [[0, 1, -1], [-1, -1, 2]]
    
    three_sum([0, 0, 0, 5, -5]) ➞ [[0, 0, 0], [0, 5, -5]]
    
    three_sum([1, 2, 3]) ➞ []
    
    three_sum([1]) ➞ []

### Notes

  * The original list **may contain duplicate numbers**.
  * Each three-element sublist in your output should be **distinct**.
  * Sublists should be ordered by the first element of the sublist.
  * Sublists themselves should be ordered the same as the original list.
  * Return an empty list if no three elements sum to zero.
  * Return an empty list if there are fewer than three elements.

"""

import itertools
import collections
def three_sum(lst):
    perm = (itertools.combinations(lst, 3))
    fin_lst = list(collections.OrderedDict.fromkeys([i for i in perm if sum(i) == 0]))
    return [list(i) for i in fin_lst]

