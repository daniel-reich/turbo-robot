"""


Given a list of integers, find the pair of adjacent elements that have the
largest product and return that product.

### Examples

    adjacent_product([3, 6, -2, -5, 7, 3] ) ➞ 21
    
    adjacent_product([5, 6, -4, 2, 3, 2, -23]) ➞ 30
    
    adjacent_product([0, -1, 1, 24, 1, -4, 8, 10]) ➞ 80

### Notes

Each list has at least two elements.

"""

def adjacent_product(lst):
  a = []
  for x in range(len(lst)-1):
    a.append(lst[x]*lst[x+1])
  return max(a)

