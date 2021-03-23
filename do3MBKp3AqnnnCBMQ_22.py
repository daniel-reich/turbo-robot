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
  import random
  ls = []
  while True:
    x = random.randint(1, 5)
    if not str(x) in ls:
      ls.append(str(x))
    if len(ls)==5:
      return int("".join(ls))

