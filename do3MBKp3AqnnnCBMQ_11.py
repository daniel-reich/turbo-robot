"""


Create a function that produces a random number that contains all numbers from
one to five, without any duplicates.

### Examples

    12345
    
    21345
    
    51234

### Notes

N/A

"""

def numbers():
  from itertools import permutations as p
  from random import randint as r
  
  perms = list(p(['1','2','3','4','5'], 5))
  
  return int(''.join(perms[r(1, len(perms))]))

