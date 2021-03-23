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
def product(num):    
    return reduce(lambda x,y:x*y,[int(i) for i in str(num)])
​
​
def max_product(num):
    greater_value = 0
    lst = []
    for n in range(num+1):
        mul= product(n)
        if mul > greater_value:
            greater_value = mul
            lst = [n]
        elif mul == greater_value:
            lst.append(n)
    return lst

