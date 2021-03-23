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

from functools import reduce
def max_product(n):
    max = 1
    for i in range(n+1):
        if prods(i) > max:
            max = prods(i)
    return [i for i in range(n+1) if prods(i) == max]
​
def prods(n):
    return int(reduce(lambda x,y: int(x)*int(y), str(n)))

