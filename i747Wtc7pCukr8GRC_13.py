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

from itertools import combinations
​
result = lambda f, x: f(a*b*c for (a,b,c) in combinations(x, 3))
​
def max_product(numbers):
    '''
    Returns the maximum product of 3 numbers in list numbers
    '''
    return result(max, numbers)
​
def min_product(numbers):
    '''
    Returns the minimum product of 3 numbers in list numbers
    '''
    return result(min, numbers)

