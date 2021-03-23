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
  perms = list(set([int("".join(list(y))) for y in permutations([x for x in str(num)])]))
  perms.sort()
  found = perms.index(num)
  if found == len(perms)-1 or perms[-1] == num:
    return perms[found]
  else:
    return perms[found+1]

