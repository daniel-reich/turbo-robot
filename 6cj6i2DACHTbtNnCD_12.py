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

def find(lst, value, start=0):
  for i in range(start, len(lst)):
    if lst[i] == value:
      return i
  return -1
  
def two_product(lst, n):
  for i in range(len(lst)):
    q, r = divmod(n, lst[i])
    if r == 0 and find(lst, q, i) > 0:
      return sorted([lst[i], q])
  return None

