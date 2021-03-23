"""


Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.

### Examples

    odd_square_patch([
      [1, 2, 4, 9],
      [4, 5, 5, 7],
      [3, 6, 1, 7]
    ]) ➞ 2
    
    # The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).
    
    odd_square_patch([[1, 2, 4, 9]]) ➞ 1
    
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.
    
    odd_square_patch([[2, 4, 6]]) ➞ 0

### Notes

N/A

"""

def odd_square_patch(lst):
  n = len(lst)
  m = len(lst[0])
  d = {(i,j):0 for i in range(n) for j in range(m) if lst[i][j]%2}
  for i,j in d.keys():
    for k in range(1,min(n,m)+1):
      if all((i+r,j+s) in d.keys() for r in range(k) for s in range(k)):
        d[i,j]+=1
  return max(d.values()) if d else 0

