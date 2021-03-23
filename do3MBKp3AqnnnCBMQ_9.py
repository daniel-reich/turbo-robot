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
  lst = []
  while len(lst)<5:
    temp = randint(1,5)
    if temp not in lst:
      lst.append(temp)
  return int(''.join([str(i) for i in lst]))

