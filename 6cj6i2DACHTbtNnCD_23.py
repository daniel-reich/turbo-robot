"""


Create a function that takes a list `lst` and a number `n` and returns a list
of two integers whose product is that of the number `n`.

### Examples

    two_product([1, 2, 3, 4, 13, 5], 39) ➞ [3, 13]
    
    two_product([11, 2, 7, 3, 5, 0], 55) ➞ [5, 11]
    
    two_product([100, 12, 4, 1, 2], 15) ➞ None

### Notes

  * No duplicates.
  * Sort the number.
  * Try doing this with 0(n) time complexity.
  * The list can have multiple solutions, so return the first match you find.

"""

def two_product(lst, n):
  lst1 = lst
  lst2 = lst
  l = []
  for i in lst:
    for j in lst:
      l.append([i,j])
​
  x = sorted([i for i in l if i[0] * i[1] == n]) 
  if len(x) == 0:
    return None
  return x[0]

