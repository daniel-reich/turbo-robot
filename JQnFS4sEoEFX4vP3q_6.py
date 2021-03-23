"""


 **Mubashir** needs your help in a simple task of multiplication of elements
in a given list.

Create a function which takes a list of integers `lst` and a positive integer
`k` and returns the **minimum and maximum possible product of k elements**
taken from the list. If enough elements are not available in the list, return
`None`.

### Examples

    product_pair([1, -2, -3, 4, 6, 7], 1) ➞ (-3, 7)
    
    product_pair([1, -2, -3, 4, 6, 7], 2) ➞ (-21, 42)
    # -3*7, 6*7
    
    product_pair([1, -2, -3, 4, 6, 7], 3) ➞ (-126, 168)
    # -3*6*7, 4*6*7
    
    product_pair([1, -2, -3, 4, 6, 7], 7) ➞ None
    # There are only 6 elements in the list

### Notes

N/A

"""

import itertools
​
def get_prod(A):
    p = 1
    for a in A:
        p *= a
    return p
​
def product_pair(lst, k):
    if len(lst) < k:
        return 
    low, high = 2**31, -2**31
    for comb in itertools.combinations(lst, k):
        p = get_prod(comb)
        low = min(low, p)
        high = max(high, p)
    return (low, high)

