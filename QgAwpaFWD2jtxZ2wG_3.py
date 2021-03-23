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
  if abs(n) < 10:
    return 1
  return sum_digits(n / 10) + 1

