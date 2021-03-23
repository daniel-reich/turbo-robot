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
  result = []
  while len(result) < 5:
    x = random.randint(1,5)
    if str(x) not in result:
      result.append(str(x))
  return int("".join(result))

