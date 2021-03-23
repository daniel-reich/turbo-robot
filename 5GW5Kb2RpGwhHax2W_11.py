"""


Create a function that takes a two-dimensional list as an argument and returns
a one-dimensional list with the values of the original 2d list that are
arranged by spiralling through it (starting from the top-left).

### Examples

    spiral_transposition([
      [7, 2],
      [5, 0]
    ])
    
    ➞ [7, 2, 0, 5]
    
    spiral_transposition([
      [1, 2, 3],  
      [4, 5, 6],
      [7, 8, 9]
    ])
    
    ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_transposition([
      [1, 1, 1],  
      [4, 5, 2],
      [3, 3, 2] 
    ])
    
    ➞ [1, 1, 1, 2, 2, 3, 3, 4, 5]

### Notes

If you do not understand the instructions, write the 3x3 list example on a
piece of paper and trace the output through it.

"""

def spiral_idx(m,n,b):
  print(m,n)
  ret=[]
  if m<=0 or n<=0:
    return []
  ret+=[[b+0,b+x] for x in range(n)]
  #print(ret)
  if n>1:
    ret+=[[b+x,b+n-1] for x in range(1,m)]
  #print(ret)
  if m>1:
    ret+=[[b+m-1,b+x] for x in range(n-2 if n>1 else 0,-1,-1)]
  #print(ret)
  ret+=[[b+x,b+0] for x in range(m-2,0,-1)]
  #print(ret)
  return ret+spiral_idx(m-2,n-2,b+1)
​
def spiral_transposition(l):
  m=len(l)
  if isinstance(l[0],list):
    n=len(l[0])
  else:
    return 'Error: input not a 2-dim list'
  idx=spiral_idx(m,n,0)
  ret=list(map(lambda x: l[x[0]][x[1]],idx))
  return ret

