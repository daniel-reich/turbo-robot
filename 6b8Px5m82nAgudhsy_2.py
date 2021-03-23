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

import itertools as it
def next_number(n):
  if n<10:return n
  s=str(n)
  l=sorted(set(it.permutations(s,len(s))))
  p=l.index(tuple(s))
  return int(''.join(l[p+1]))if p!=len(l)-1else n

