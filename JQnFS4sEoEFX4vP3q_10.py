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

def product_pair(lst, k):
​
    num_1 = 1
    min_num, max_num = 99999, -99999
​
    import itertools
    lst_1 = list(itertools.combinations(lst, k))
​
    if len(lst) < k:
        return None
    else:
        for x in lst_1:
            for y in x:
                num_1 *= y
            if num_1 < min_num:
                min_num = num_1
            if num_1 > max_num:
                max_num = num_1
            num_1 = 1
​
    return (min_num, max_num)

