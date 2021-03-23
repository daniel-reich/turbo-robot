"""


Create a function that takes four lists as arguments and returns a count of
the total number of identical lists.

### Examples

    count_identical_lists([0, 0, 0], [0, 1, 2], [0, 0, 0], [2, 1, 0]) ➞ 2
    
    count_identical_lists([0, 1, 0], [0, 1, 2], [0, 2, 0], [2, 1, 0]) ➞ 0
    
    count_identical_lists([0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]) ➞ 3

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're really stuck, unlock solutions in the **Solutions** tab.

"""

import itertools
​
def count_identical_lists(lst1, lst2, lst3, lst4):
  cnt=0
  for x,y in itertools.combinations([lst1,lst2,lst3,lst4],2):
    if x==y: cnt+=1
  if not cnt: return 0
  for i in range(1,5):
    if sum(range(i+1))==cnt:
      return i+1

