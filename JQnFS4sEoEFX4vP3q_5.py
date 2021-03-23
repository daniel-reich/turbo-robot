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

from functools import reduce
def product_pair(lst, k):
    len_lst = len(lst)
    if len_lst < k:
        return None
    elif len_lst == k:
        res = reduce(lambda a, b: a * b, lst)
        return res, res
    elif k == 1:
        return min(lst), max(lst)
    lst.sort(key=lambda x: abs(x), reverse=True)
    prod_k = reduce(lambda a, b: a * b, lst[:k])
    if prod_k > 0:
        res_max = prod_k
        positive_k1 = lst[k - 1] > 0
        for i in range(k, len_lst):
            if positive_k1 and lst[i] <= 0:
                res = reduce(lambda a, b: a * b, lst[:k - 1]) * lst[i]
                return res, res_max
            elif not positive_k1 and lst[i] >= 0:
                res = reduce(lambda a, b: a * b, lst[:k - 1]) * lst[i]
                return res, res_max
        res_min = reduce(lambda a, b: a * b, lst[-k:])
        return res_min, res_max
    elif prod_k < 0:
        res_min = prod_k
        positive_k1 = lst[k - 1] > 0
        for i in range(k, len_lst):
            if positive_k1 and lst[i] <= 0:
                res = reduce(lambda a, b: a * b, lst[:k - 1]) * lst[i]
                return res_min, res
            elif not positive_k1 and lst[i] >= 0:
                res = reduce(lambda a, b: a * b, lst[:k - 1]) * lst[i]
                return res_min, res
        res_max = reduce(lambda a, b: a * b, lst[-k:])
        return res_min, res_max
    return 0, 0

