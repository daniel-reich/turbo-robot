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
import numpy
​
def product_pair(lst, k):
    max_value = 0
    min_value = 0
    outputlist = []
​
    if k > len(lst) or len(lst) == 0:
        return None
    elif k == len(lst):
        max_value = numpy.prod(lst)
        min_value = numpy.prod(lst)
    else:
        onetime = True
        for i in itertools.combinations(lst, k):
            if onetime == True:
                max_value = numpy.prod(i)
                min_value = numpy.prod(i)
                onetime = False
            answer = numpy.prod(i)
            if answer > max_value:
                max_value = answer
            elif answer < min_value:
                min_value = answer
    outputlist.append(min_value)
    outputlist.append(max_value)
    return tuple(outputlist)

