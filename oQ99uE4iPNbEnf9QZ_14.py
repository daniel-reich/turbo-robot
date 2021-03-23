"""


Given a known number of unique items, how many ways could we arrange them in a
row?

Create a function that takes an integer `n` and returns the number of digits
of the number of possible permutations for `n` unique items. For instance, 5
unique items could be arranged in 120 unique ways. 120 has 3 digits, hence the
integer `3` is returned.

### Examples

    no_perms_digits(0) ➞ 1
    
    no_perms_digits(1) ➞ 1
    
    no_perms_digits(5) ➞ 3
    
    no_perms_digits(8) ➞ 5

### Notes

This challenge requires some understanding of combinatorics.

"""

def no_perms_digits(n):
  sum_out= 1
  s = 0
  for i in range(n,0,-1):
    sum_out *= i 
  s = len(str(sum_out))
  return s

