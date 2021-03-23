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
  num = random.randrange(12345,54321)
  while(not str(num).count('5') == 1 or not str(num).count('4') == 1 or not str(num).count('3') == 1 or not str(num).count('2') == 1 or not str(num).count('1') == 1):
    num = random.randrange(12345,54321)
  return num

