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

def calc(lst, i, k) :
    c = 0
    res = []
    for j in range(i, len(lst)):
        if lst[j] == 1:
            c += 1
        elif k > 0:
            c += 1
            k -= 1
            res.append(j) 
        elif k == 0:
            return c, res
    return c, res
    
def zero_indices(lst, k):
    maxi = 0
    for i in range(len(lst)) :
        c, tmp = calc(lst, i, k)
        print(i, c, tmp) 
        if c > maxi :
            maxi = c
            res = [h for h in tmp]
    return res

