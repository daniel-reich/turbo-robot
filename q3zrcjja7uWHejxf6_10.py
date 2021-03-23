"""


Create a function that takes a string containing integers as well as other
characters and return the sum of the negative integers only.

### Examples

    negative_sum("-12 13%14&-11") ➞ -23
    # -12 + -11 = -23
    
    negative_sum("22 13%14&-11-22 13 12") ➞ -33
    # -11 + -22 = -33

### Notes

There is at least one negative integer.

"""

def negative_sum(chars):
    nums = [int(_) for _ in  ''.join([c  if c in "+-0123456789" else ' ' for c in chars]).replace('-', ' -').split()]
    return sum([n for n in nums if n < 0])

