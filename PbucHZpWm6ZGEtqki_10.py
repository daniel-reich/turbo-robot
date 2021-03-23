"""


Create a function that returns the subarrays of `n` consecutive elements from
the original element that sum up to `k`. The function will have the following
form: `sliding_sum(lst, n, k)`

To illustrate:

    sliding_sum([3, 4, 1, 9, 9, 0, 3, 5, 4], 3, 8) ➞ [[3, 4, 1], [0, 3, 5]]
    # Where [3, 4, 1] and [0, 3, 5] are the only subarrays that sum to 8 with length 3.

### Examples

    sliding_sum([1, 4, 2, 3, 5, 0], 2, 5) ➞ [[1, 4], [2, 3], [5, 0]]
    
    sliding_sum([5, 5, 5, 5, 5], 1, 5) ➞ [[5], [5], [5], [5], [5]]
    
    sliding_sum([5, 5, 5, 5, 5], 5, 24) ➞ []

### Notes

Return an empty array if no subarrays satisfy the `(n,k)` condition.

"""

import numpy as np
def sliding_sum(lst, n, k):
  final_lst = []
  for i in range(len(lst)-1):
    if sum(lst[i:i+n]) == k:
      final_lst.append(lst[i:i+n])
  if all(np.array(lst)==k) and n == 1:
    final_lst.append([lst[-1]])
    return final_lst
  else:
    return final_lst

