"""


You are given a **list of binary integers** and `k`, the **number of flips**
allowed.

Write a function that returns the indices of zeroes of which, when flipped,
return the **longest contiguous sequence of ones**.

### Examples

    zero_indices([1, 0, 1, 1, 0, 0, 0, 1], 1) ➞ [1]
    
    zero_indices([1, 0, 0, 0, 0, 1], 1) ➞ [1]
    
    zero_indices([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 3) ➞ [6, 7, 9]
    
    zero_indices([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 3) ➞ [7, 8, 9]

### Notes

If multiple combinations of indices tie for longest one sequence, return the
indices which occur **first** (see examples #2, #3).

"""

from itertools import combinations
def zero_indices(lst, k):
​
    def max_ones(arr):
        z, curr = 0, 0
        for i in range(len(arr)):
            if arr[i] == 1:
                curr += 1
                if curr > z:
                    z = curr
            else:
                curr = 0
        return z
​
    longest = (0, [])
    for cmb in combinations([i for i, d in enumerate(lst) if d == 0], k):
        mxz = max_ones([1 if i in cmb else lst[i] for i in range(len(lst))])
        if mxz > longest[0]:
            longest = (mxz, list(cmb))
    return longest[1]

