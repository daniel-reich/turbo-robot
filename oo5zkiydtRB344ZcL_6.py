"""


Create a function that returns how many times it's been called previously. Do
not use a global variable.

### Examples

    counter() ➞ 0
    
    counter() ➞ 1
    
    counter() ➞ 2

### Notes

The first time it's called, the function should return `0`.

"""

def counter():
  if hasattr(counter, 'c') == False:
    counter.c = -1
  counter.c += 1
  return counter.c

