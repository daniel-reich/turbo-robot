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

import random
def numbers():
  v = []
  while True:
    x = random.randint(1,5)
    if x not in v:
      v.append(x)
    if set(v) == {1,2,3,4,5}:
      break
  return sum(n*10**i for i, n in enumerate(v))

