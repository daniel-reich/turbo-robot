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

def products(lst):
  products = []
  for i in range(0,len(lst)-2):
    for j in range(i+1,len(lst)-1):
      for k in range(j+1,len(lst)):
        products.append(lst[i] * lst[j] * lst[k])
  return products
​
def max_product(lst):
  return max(products(lst))
  
def min_product(lst):
  return min(products(lst))

