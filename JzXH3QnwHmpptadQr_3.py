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

bitwise_logical_negation=lambda x:1>>x*x

