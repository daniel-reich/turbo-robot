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
    sign = 1 if num >= 0 else -1
    num, res, power = abs(num), [], 0
    while num:
        num, rem = divmod(num, 10)
        res.append(sign * rem * pow(10, power))
        power += 1
    return res[::-1]

