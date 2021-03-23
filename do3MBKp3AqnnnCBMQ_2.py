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
  num = ""
  while len(num) < 5:
    temp = str(randint(1, 5))
    num += temp if temp not in num else ''
  return int(num)

