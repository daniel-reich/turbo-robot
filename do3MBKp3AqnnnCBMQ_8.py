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

from random import shuffle
def numbers():
    lst = list(range(1, 6))
    shuffle(lst)
    return int("".join(map(str, lst)))

