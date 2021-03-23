"""


Fibonacci numbers are created in the following way:

    F(0) = 0
    F(1) = 1
    ...
    F(n) = F(n-2) + F(n-1)

Write a function that calculates the `nth` Fibonacci number.

### Examples

    fib(0) ➞ 0
    
    fib(1) ➞ 1
    
    fib(2) ➞ 1
    
    fib(8) ➞ 21

### Notes

N/A

"""

def fib(n):
  if n == 0:
    return 0
  a = 0
  b = 1
  c = 1
  for i in range(0,n):
    a = b
    b = c
    c = a + b
  return a

