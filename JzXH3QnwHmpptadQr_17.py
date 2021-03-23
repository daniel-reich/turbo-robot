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
  return ~((x&1)|((x>>1)&1)|((x>>2)&1)|((x>>3)&1)|((x>>4)&1)|((x>>5)&1)|((x>>6)&1)|((x>>7)&1)|((x>>8)&1))&1

