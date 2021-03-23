"""


Write **two** functions:

  1. One that returns the **maximum product** of three numbers in a list.
  2. One that returns the **minimum product** of three numbers in a list.

### Examples

    max_product([-8, -9, 1, 2, 7]) ➞ 504
    
    max_product([-8, 1, 2, 7, 9]) ➞ 126
    
    min_product([1, -1, 1, 1]) ➞ -1
    
    min_product([-5, -3, -1, 0, 4]) ➞ -15

### Notes

N/A

"""

import itertools
import numpy as np
​
def max_product(lst):
    perm = list(itertools.permutations(lst, 3))
    all_prods = [np.prod(i) for i in perm]
    return max(all_prods)
​
def min_product(lst):
    perm = list(itertools.permutations(lst, 3))
    all_prods = [np.prod(i) for i in perm]
    return min(all_prods)

