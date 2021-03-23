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

from random import *
​
def numbers():
  nums = list(range(1, 6))
  shuffle(nums)
  return int(''.join(map(str, nums)))

