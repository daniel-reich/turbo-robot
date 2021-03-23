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
    sign = 1
    if num < 0:
        sign = -1
        num = -num    
    n = len(str(num))
    ans = []
    for p in range(n - 1, -1, -1):
        p10 = 10**p
        ans.append(sign * (num // p10) * p10)
        num %= p10
    return ans

