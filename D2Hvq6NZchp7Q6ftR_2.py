"""


Create a function which returns the Modulo of the two given numbers.

### Examples

    mod(-13, 64) ➞ 51
    
    mod(50, 25) ➞ 0
    
    mod(-6, 3) ➞ 0

### Notes

All test cases contain valid numbers.

"""

def mod(m, n):
    return mod(m + n, n) if m < 0 else m if m < n else mod(m - n, n)

