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

def counter() -> int:
  if not hasattr(counter, 'count'):
    counter.count = 0
  counter.count += 1
  return counter.count - 1

