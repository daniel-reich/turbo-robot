"""


Create a function that takes a number `num` and returns its length.

### Examples

    number_length(10) ➞ 2
    
    number_length(5000) ➞ 4
    
    number_length(0) ➞ 1

### Notes

 **The use of the len() function is prohibited.**

"""

def number_length(n):
  out = 0
  while n >= 1:
    n /= 10
    out += 1
  if n == 0: out += 1
  return out

