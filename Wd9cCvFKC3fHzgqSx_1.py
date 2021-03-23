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
    sign, lst = 1 if num >= 0 else -1, list(map(int,str(abs(num))))
    return [sign * lst[i] * 10**(len(lst)-i-1) for i in range(len(lst))]

