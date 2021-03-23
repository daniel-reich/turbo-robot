"""


Given a list of numbers, return the _pair_ of numbers that give the minimum
absolute _difference_. Return the pair as a _list_ , sorted in _ascending_
order. If multiple pairs have the same difference, return the pair with the
smallest sum.

### Examples

    min_difference_pair([40, 16, 8, 17, 15]) ➞ [15, 16]
    # [15, 16] has smaller sum than [16, 17]
    
    min_difference_pair([1, -31, -27, -18, -48, -15, -11, -34]) ➞ [-34, -31]
    
    min_difference_pair([0, 2, 35, 42, 45, 14, -6, -1]) ➞ [-1, 0]
    
    min_difference_pair([32, 33, 4, 6, 48, 18, 20, -7, -4, 31]) ➞ [31, 32]

### Notes

There will be no duplicate numbers in the list.

"""

from itertools import combinations
def min_difference_pair(nums):
  a=nums
  b=list(combinations(a,2))
  c=[]
  for i in range(len(b)):
      x=abs(b[i][0]-b[i][1])
      c.append([b[i],x])
  y=sorted(c,key=lambda x:x[1])
  z=(y[0][1])
  w=[]
  for i in range(len(y)):
      if y[i][1]==z:
          w.append(y[i][0])
  m=[]
  for i in range(len(w)):
      m.append([w[i],sum(w[i])])
  n=sorted(m,key=lambda x:x[1])
  p=list((n[0][0]))
  p.sort()
  return(p)

