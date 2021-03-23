"""


Create a function that takes two integers, `num` and `n`, and returns an
integer which is divisible by `n` and is the closest to `num`. If there are
two numbers equidistant from `num` and divisible by `n`, select the larger
one.

### Examples

    round_number(33, 25) ➞ 25
    
    round_number(46, 7) ➞ 49
    
    round_number(133, 14) ➞ 140

### Notes

`n` will always be a positive number.

"""

def round_number(num, n):
    lower = 0
    i = 1
    while True:
        x = i * n
        if x < num:
            lower = x
        else:
            upper = x
            break
        i += 1
    if num - lower < upper - num:
        return lower
    return upper

