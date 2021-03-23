"""


Write a function that returns the **smallest N-digit number** which is a
**multiple** of the specified value.

### Examples

    smallest(3, 8) ➞ 104
    # Smallest 3-digit integer that is a multiple of 8
    
    smallest(5, 12) ➞ 10008
    
    smallest(7, 1) ➞ 1000000
    
    smallest(2, 3) ➞ 12

### Notes

N/A

"""

def smallest(digits, value):
​
    n = int("1" + "0" * (digits - 1))
​
    while n % value != 0:
        n += 1
​
    return n

