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

from random import sample
​
def numbers():
  return int(''.join(sample('12345', 5)))

