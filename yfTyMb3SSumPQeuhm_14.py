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
    if n == 2:
        return 1
    s0, s1 = 0, 1
    a, b = 1, 1
    while n:
        if n % 2 == 0:
            a, b = a**2 + b**2, b*(a+(a-b))
            n /= 2
        else:
            s0, s1 == b*s0 +(a-b)*s1, a*s0 + b*s1
            n -= 1
    return b

