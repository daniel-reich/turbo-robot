"""


Given a number (positive, negative, or 0), return the logical negation (as a 1
or 0) of that number. Do so using only bitwise operators:

    (~, &, |, ^, >>, <<, etc) and +

Any of these characters/constructs are not allowed:

    if, do, while, for, -, not, or, and, is, [,] and any functions.

### Examples

    bitwise_logical_negation(1) ➞ 0
    
    bitwise_logical_negation(5) ➞ 0
    
    bitwise_logical_negation(0) ➞ 1
    
    bitwise_logical_negation(3) ➞ 0

### Notes

Use as few operators as possible for more of a challenge.

"""

def bitwise_logical_negation(x):
  x = ~x 
  x = x & (x >> 8) & 0xFF
  x = x & (x >> 4) & 0xF
  x = x & (x >> 2) & 0x3
  x = x & (x >> 1) & 0x1
  return x

