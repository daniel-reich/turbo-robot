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
    c = a+1 
    o = c%b
    if o == 0:
        return c
    else:
        for i in range(a, a*1000):
            p = i%b
            if p == 0:
                print("yes")
                return i

