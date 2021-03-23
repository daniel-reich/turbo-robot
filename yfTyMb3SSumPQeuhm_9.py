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
    arr = []
    while n:
        arr.append(n)
        n //= 2
    a, b = 0, 1
    while arr:
        c = a * ((b << 1) - a)
        d = a**2 + b**2
        n = arr.pop()
        if n%2:
            a, b = d, c + d
        else:
            a, b = c, d
    return a

