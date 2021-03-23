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
  from itertools import permutations
  if len(str(num))==1:  return num
  perms = [int(''.join(p)) for p in permutations(str(num))]
  p = sorted([x for x in set(perms)])
  return num if num==max(p) else p[p.index(num)+1]

