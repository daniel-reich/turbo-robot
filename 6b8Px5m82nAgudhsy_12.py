"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

def next_number(num):
  n = str(num)
  R = range(len(n))
  swap = [(i1,i2) for i1 in R for i2 in R if i1<i2 and int(n[i1])<int(n[i2])]
  cands = sorted(swap,key = lambda t: (int(t[0]),-int(n[t[1]])))
  if not cands: return num
  k1, k2 = cands[-1]
  return int(n[:k1]+n[k2]+"".join(sorted(n[k1:k2]+n[k2+1:])))

