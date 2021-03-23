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
    products=[]
    for i in range(len(lst)):
        for i1 in range(len(lst)):
            for i2 in range(len(lst)):
                if i!=i1 and i1!=i2 and i!=i2:
​
                
                    products.append(lst[i]*lst[i1]*lst[i2])
​
    return max(products)
​
​
​
def min_product(lst):
    products = []
    for i in range(len(lst)):
        for i1 in range(len(lst)):
            for i2 in range(len(lst)):
                if i != i1 and i1 != i2 and i != i2:
                    products.append(lst[i] * lst[i1] * lst[i2])
​
    return min(products)

