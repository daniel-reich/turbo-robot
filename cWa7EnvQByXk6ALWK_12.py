"""


The golden ratio is ubiquitous in math, science, art, and nature. This
challenge is concerned with the number itself, which is 1.618033988 to 10
significant digits. Implement a function that calculates the golden ratio to
100 significant digits using only integers, strings and basic arithmetic
operations: `+`, `-`, `*`, `//`

### Examples

    golden_ratio() ➞ 1.618033988+90 more decimal places

### Notes

This function has no argument so naturally there is only one test case.

"""

def golden_ratio():
    one_100_digits = 10**99
    fib1 = fibo(300) * one_100_digits
    fib2 = fibo(299)
    fib_str = str(fib1//fib2)
    fib_str = fib_str[0:1] + '.' + fib_str[1:]
    return fib_str                
​
def fibo(n):
    a, b = 0,1
    for x in range (n-1):
        a, b = b, a+b
    return b

