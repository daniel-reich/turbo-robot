"""


Create a function that takes a number `num` and returns each place value in
the number.

### Examples

    num_split(39) ➞ [30, 9]
    
    num_split(-434) ➞ [-400, -30, -4]
    
    num_split(100) ➞ [100, 0, 0]

### Notes

N/A

"""

def num_split(num):
    l = [int('{}{}'.format(x, '0' * i)) for i, x in enumerate(str(num)[::-1])][::-1]
    if num < 0:
        l = l[1:]
    return [-i if num < 0 else i for i in l]

