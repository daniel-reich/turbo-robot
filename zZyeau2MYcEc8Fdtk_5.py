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
    if num % n == 0:
        return num
    k = num / n
    n1 = int(k) * n
    n2 = (int(k) + 1) * n
    return n1 if num - n1 < n2 - num else n2

