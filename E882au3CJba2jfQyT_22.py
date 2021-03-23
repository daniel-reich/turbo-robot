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
  return sorted(list(set([i for i in lst1 if i in lst2])))

