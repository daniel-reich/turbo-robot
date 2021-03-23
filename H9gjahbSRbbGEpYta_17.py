"""


Create a function that takes two numbers `n1` `n2` and multiplies them
**without using** `*`.

### Examples

    multiply(3, 2) ➞ 6
    
    multiply(4, 10) ➞ 40
    
    multiply(-2, 4) ➞ -8

### Notes

Do not use `*` for this challenge.

"""

def multiply(x, y):
    if (y == 0):
        return 0 
    if (y > 0):
        return (x + multiply(x, y - 1))
    if (y < 0):
        return -multiply(x, -y)

