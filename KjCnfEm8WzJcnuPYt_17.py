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
    if k >= lst.count(0):
        return [k for k in range(len(lst)) if lst[k] == 0]
    left, count, window, leftIndex = 0, 0, 0, 0
    for right in range(len(lst)):
        if lst[right] == 0:
            count += 1
        while count > k:
            if lst[left] == 0:
                count -= 1
            left += 1
        if right - left + 1 > window:
            window = right - left + 1
            leftIndex = left
    return [k for k in range(leftIndex, min(leftIndex + window, len(lst))) if lst[k] == 0]

