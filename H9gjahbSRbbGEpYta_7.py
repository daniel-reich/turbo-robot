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

def multiply(n1, n2):
    total = 0
    x = 1 if n2>0 else -1
    while n2 != 0:
        total += n1
        n2 -= x
    return total if x==1 else total-total-total

