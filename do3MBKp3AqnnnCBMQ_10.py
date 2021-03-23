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
  l = ""
  while len(l) < 5:
    x = random.randint(1,5)
    if str(x) not in l:
      l += str(x)
  return int(l)

