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

from random import randint
def numbers():
    num = ""
    while len(num)<5:
        temp = str(randint(1,5))
        if temp not in num:
            num += temp
    return int(num)

