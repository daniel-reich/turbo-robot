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
  p=len(lst)
  q=len(lst[0])
  r=min(p,q)
  for i in range(p):
    for j in range(q):
      if lst[i][j]%2==1:
        lst[i][j]=1  
  if p==1 and 1 in lst[0]:
    return 1
  for x in range(r,0,-1):
    ans=''
    for y in range(p):
      sy=''.join(str(b) for b in lst[y])
      if '1'*x in sy:
        ans+=str(x)
      else:
        ans+='0'
    if str(x)*x in ans:
      return x
  return 0

