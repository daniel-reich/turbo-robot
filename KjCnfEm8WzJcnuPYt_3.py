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

def zero_indices(lst, k):
    serie = [0, []]  # special case if array does not contain 1 | put index directly if K = 0
    for idx, elm in enumerate(lst):
        flips = k
        serie_len = 0
        flip_idx = []
​
        for sub_idx, sub_elm in enumerate(lst[idx:]):
            if sub_elm == 0 and flips <= 0: break
            if sub_elm == 0 and flips > 0:
                flips = flips - 1
                flip_idx.append(idx + sub_idx)
            serie_len += 1
​
        if serie_len > serie[0]: serie = [serie_len, flip_idx]
    return serie[1]

