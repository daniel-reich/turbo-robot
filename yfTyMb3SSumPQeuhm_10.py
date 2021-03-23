"""


Write a function that efficiently calculates Fibonacci terms.

### Examples

    fibonacci(1) ➞ 1
    
    fibonacci(2) ➞ 1
    
    fibonacci(4) ➞ 3
    
    fibonacci(64) ➞ 10610209857723

### Notes

The input will always be a power of two.

"""

def fibonacci(n):
    a, b, c = 1, 1, 2
    while n > 2:
        a, b = a*a + b*b, a*b + b*c
        c = a + b
        n //= 2
    return b

