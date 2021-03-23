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
  count=0
  if n==0:
    return 1
  while n!=0:
    n//=10
    count+=1
  return count

