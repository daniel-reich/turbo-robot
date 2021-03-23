"""


Create a function that takes an integer and returns the factorial of that
integer. That is, the integer multiplied by all positive lower integers.

### Examples

    factorial(3) ➞ 6
    
    factorial(5) ➞ 120
    
    factorial(13) ➞ 6227020800

### Notes

Assume all inputs are greater than or equal to 0.

"""

def factorial(n):
# Base case: 1! = 1
    if n == 1 or n == 0:
        return 1
​
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

