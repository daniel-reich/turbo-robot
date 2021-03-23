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
    s = []
    i = len(str(abs(num)))
    while i != 0:
        if num > 0:
            s.append(num//(10**(i-1))*(10**(i-1)))
            num -= num//(10**(i-1))*(10**(i-1))
            i -= 1
        else:
            s.append(-(abs(num) // (10 ** (i - 1)) * (10 ** (i - 1))))
            num += abs(num) // (10 ** (i - 1)) * (10 ** (i - 1))
            i -= 1
    return s

