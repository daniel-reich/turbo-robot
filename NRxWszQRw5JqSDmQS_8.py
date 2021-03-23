"""


Given two integers, `a` and `b`, return `True` if `a` can be divided evenly by
`b`. Return `False` otherwise.

### Examples

    divides_evenly(98, 7) ➞ True
    # 98/7 = 14
    
    divides_evenly(85, 4) ➞ False
    # 85/4 = 21.25

### Notes

`a` will always be greater than or equal to `b`.

"""

divides_evenly = lambda a, b: a % b < 1

