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

import itertools
def mult(j):
    h = 1
    for i in j:
        h=h*i
    return h
def max_product(lst):
    l = []
    for i in range(len(lst)+1):
        for j in itertools.combinations(lst,i):
            if len(j)==3:l.append(mult(list(j)))
    return max(l)
def min_product(lst):
    l = []
    for i in range(len(lst)+1):
        for j in itertools.combinations(lst,i):
            if len(j)==3:l.append(mult(list(j)))
    return min(l)

