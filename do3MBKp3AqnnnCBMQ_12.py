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

from itertools import permutations as P
import random
def numbers():
  A=list(P(range(1, 6)))
  return int(''.join([str(k) for k in A[random.randint(0,len(A)-1)]]))

