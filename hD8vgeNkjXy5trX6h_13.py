"""


Create a function that returns all **combinations of size n** from a list.
Sort the list in ascending lexicographical order.

### Examples

    combo([1, 2, 3, 4], 1) ➞ [[1], [2], [3], [4]]
    
    combo([1, 2, 3, 4], 2) ➞ [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    
    combo([1, 2, 3, 4], 5) ➞ []
    
    combo([1, 2, 3, 4], 0) ➞ [[]]

### Notes

  * Lexicographical order: Compare the first element: `[1, 2]` will be before `[2, 4]`. If both share the same first element, compare the second element: `[1, 2]` is before `[1, 3]`, etc.
  * Return an empty list `[]` if `n` exceeds the length of the list.
  * Return `[[]]` if `n` is `0` (see example #4). (Since there is only one combination of length 0: an empty list).

"""

from itertools import permutations
from itertools import chain
from collections import Counter
def combo(lst, n):
  a=len(lst)
  newLst=[]
  outLst=[]
  if(n>a):
    return newLst
  else:
    subLst=[]
    if(n==0):
      newLst.append(subLst)
      return newLst
    else:
      perm = permutations(lst, n)
      z=sorted(set(perm))
      print("sorted unique permutations is: "+str(z))
      y=len(z)
      for i in range(0,y):
        x=z[i]
        w=sorted(x)
        newLst.append(w)
  outLst=Counter([tuple(q) for q in newLst])
  g=list(sorted(outLst.keys()))
  sLst=[]
  xLst=[]
  h=len(g)
  print(h)
  for k in range(0,h):
      m=g[k]
      p=len(m)
      print(p)
      for f in range(0,p):
          sLst.append(m[f])
      xLst.append(sLst)
      sLst=[]
  return xLst

