"""


Write a function that returns all numbers **less than or equal to N** with the
maximum product of digits.

### Examples

    max_product(8) ➞ [8]
    
    max_product(27) ➞ [27]
    
    max_product(211) ➞ [99, 199]
    
    max_product(9578) ➞ [8999]

### Notes

Search for numbers in the range: `[0, n]`.

"""

import numpy
def max_product(num):
 prod1={i:numpy.prod([int(j) for j in str(i)]) for i in range(0,num+1)}
 max1=max(prod1.values())
 keylist=[key for (key,value) in prod1.items() if value==max1]
 return keylist

