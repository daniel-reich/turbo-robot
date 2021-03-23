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

from itertools import combinations
​
​
def product_pair(lst, k):
    if k > len(lst):
        return None
    if k == 1:
        sort_lst = sorted(lst)
        return (sort_lst[0], sort_lst[-1])
    total_lst = list(combinations(lst, k))
    res = sorted([lst_mul(i) for i in total_lst])
    return (res[0], res[-1])
​
​
def lst_mul(lst):
    sum_to = 1
    for i in lst:
        sum_to *= i
    return sum_to

