"""


Write a function that calculates the **factorial** of a number
**recursively**.

### Examples

    factorial(5) ➞ 120
    
    factorial(3) ➞ 6
    
    factorial(1) ➞ 1
    
    factorial(0) ➞ 1

### Notes

N/A

"""

def factorial(n):
# Base case: 1! = 1
  if n == 1 or n == 0:
    return 1
# Recursive case: n! = n * (n-1)!
  else:
    return n * factorial(n-1)

