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
    x = []
    is_neg = False
    if num < 0:
        num *= -1
        is_neg = True
    y = str(num)
    for i in range(len(y)):
        x += [int(y[i]) * 10**(len(y)-i-1)]
    if is_neg:
        x = [-i for i in x]
    return x

