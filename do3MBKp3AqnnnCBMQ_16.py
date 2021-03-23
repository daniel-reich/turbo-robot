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

from itertools import permutations as perms
import random
def numbers():
    lon =  [''.join(n) for n in perms('12345')]
    return int(random.choice(lon))

