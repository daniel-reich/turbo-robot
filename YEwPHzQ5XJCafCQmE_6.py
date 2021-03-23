"""


Given a string, return `True` if its length is even or `False` if the length
is odd.

### Examples

    odd_or_even("apples") ➞ True
    
    odd_or_even("pears") ➞ False
    
    odd_or_even("cherry") ➞ True

### Notes

N/A

"""

def odd_or_even(word):
  return len(word) % 2 == 0

