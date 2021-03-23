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

from itertools import permutations
import random
pool = [int(''.join(str(d) for d in perm)) for perm in permutations(range(1,6),5)]
​
def numbers():
  return pool[random.randrange(0,59)]

