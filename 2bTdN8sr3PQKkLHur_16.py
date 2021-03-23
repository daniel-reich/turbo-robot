"""


You are given two numbers `a` and `b`. Create a function that returns the next
number greater than `a` and `b` and divisible by `b`.

### Examples

    divisible_by_b(17, 8) ➞ 24
    
    divisible_by_b(98, 3) ➞ 99
    
    divisible_by_b(14, 11) ➞ 22

### Notes

`a` will always be greater than `b`.

"""

def divisible_by_b(a, b):
    i=a
    while i>=a:
        if i%b==0:
            return i
        i=i+1

