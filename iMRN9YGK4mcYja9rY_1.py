"""


Create a function that takes a list and returns a list of the accumulating
product.

### Examples

    accumulating_product([1, 2, 3, 4]) ➞ [1, 2, 6, 24]
    # [1, 2, 6, 24] can be written as [1, 1 x 2, 1 x 2 x 3, 1 x 2 x 3 x 4]
    
    accumulating_product([1, 5, 7]) ➞ [1, 5, 35]
    
    accumulating_product([1, 0, 1, 0]) ➞ [1, 0, 0, 0]
    
    accumulating_product([]) ➞ []

### Notes

An empty list should return an empty list `[]`.

"""

def accumulating_product(lst):
  temp = []
  if len(lst) == 0:
    return temp
  a = 1
  for item in lst:
    a *= item
    temp.append(a)
    
  return temp

