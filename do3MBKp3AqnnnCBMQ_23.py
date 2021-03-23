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
​
def numbers():
    A = ['1', '2', '3', '4', '5']
    random.shuffle(A)
    return int(''.join(A))

