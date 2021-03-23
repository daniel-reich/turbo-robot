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

def two_product(l, n):
  l=[i for i in l if i!=0]
  a=[i for i in l if n%i==0 and i!=1 and i!=-1]
  b=[i for i in a if n/i in a]
  if b==[]:
    return None
  else:
    return sorted(b)

