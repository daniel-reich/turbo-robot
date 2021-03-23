"""


Create a function that takes two lists of numbers sorted in ascending order
and returns a list of numbers which are common to both the input lists.

### Examples

    common_elements([-1, 3, 4, 6, 7, 9], [1, 3]) ➞ [3]
    
    common_elements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]) ➞ [1, 3, 4, 7]
    
    common_elements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]) ➞ [1, 2, 4, 5]
    
    common_elements([1, 2, 3, 4, 5], [10, 12, 13, 15]) ➞ []

### Notes

  * Lists are sorted.
  * Try doing this problem with O(n + m) time complexity.

"""

def common_elements(lst1, lst2):
  it1, it2 = (i for i in lst1), (i for i in lst2)
  el1, el2 = next(it1, None), next(it2, None)
  common = []
  while None not in (el1, el2):
    if el1 > el2:
      el2 = next(it2, None)
    elif el1 < el2:
      el1 = next(it1, None)
    else:
      common.append(el1)
      el1, el2 = next(it1, None), next(it2, None)
  return common

