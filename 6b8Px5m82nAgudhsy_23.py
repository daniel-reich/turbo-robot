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

from itertools import permutations
def next_number(num):
 numst=str(num)
 if len(numst)==1:return int(numst)
 for l in range(2,len(numst)+1):
  perms=sorted(["".join(i) for i in permutations(numst[-l:])])
  if numst[-l:]!=perms[-1]:
   if l==len(numst):
       perms = sorted(list(set(perms)))
       return int(perms[perms.index(numst) + 1])
   elif l>2:
       return int(numst[0:-l]+perms[perms.index(numst[-l:]) + 1])
   return int(numst[0:-l]+perms[-1])
 return int(numst)

