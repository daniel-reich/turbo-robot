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
    from random import randint
    from itertools import permutations
    buf = set(''.join(x) for x in permutations('12345', 5))
    return int(list(buf)[randint(1, len(buf))])

