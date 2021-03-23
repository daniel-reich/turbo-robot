"""


Write **two** functions:

  1. One that returns the **maximum product** of three numbers in a list.
  2. One that returns the **minimum product** of three numbers in a list.

### Examples

    max_product([-8, -9, 1, 2, 7]) ➞ 504
    
    max_product([-8, 1, 2, 7, 9]) ➞ 126
    
    min_product([1, -1, 1, 1]) ➞ -1
    
    min_product([-5, -3, -1, 0, 4]) ➞ -15

### Notes

N/A

"""

def max_product(lst):
    prod = -99999999999999999999
​
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                prod = max(prod, lst[i] * lst[j] * lst[k])
    return prod
​
​
def min_product(lst):
    prod = 99999999999999999999
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                prod = min(prod, lst[i] * lst[j] * lst[k])
    return prod

