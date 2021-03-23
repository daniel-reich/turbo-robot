"""


Given an integer `n`. Your task is to find how many digits this integer
contains without using `str` or `len` methods!

### Examples

    sum_digits(100) ➞ 3
    
    sum_digits(1000) ➞ 4
    
    sum_digits(1) ➞ 1

### Notes

N/A

"""

def sum_digits(n):
  x = 1
  while abs(n) > 9:
    n //= 10
    x += 1
  return x

