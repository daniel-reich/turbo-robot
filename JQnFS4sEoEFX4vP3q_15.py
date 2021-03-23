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
    '''
    Returns the minimum and maximum products of k elements from lst, or None
    if this is not possible
    '''
    from itertools import combinations
    from functools import reduce
​
    if k > len(lst):
        return None
​
    multiply = lambda c: reduce(lambda x,y:x*y,c,1)
    minimum, maximum = float('inf'), float('-inf')
​
    for combo in combinations(lst, k):
        product = multiply(combo)
        if product < minimum:
            minimum = product
        if product > maximum:
            maximum = product
​
    return (minimum, maximum)

