"""


Create a function that takes a string and returns `True` if the sum of the
position of every letter in the alphabet is even and `False` if the sum is
odd.

### Examples

    is_alpha("i'am king")  ➞ True
    # 9 + 1 + 13 + 11 + 9 + 14 + 7 = 64 (even)
    
    is_alpha("True") ➞ True
    # 20 + 18 + 21 + 5= 64 (even)
    
    is_alpha("alexa") ➞ False
    # 1 + 12 + 5 + 24 + 1= 43 (odd)

### Notes

  * Case insensitive.
  * Ignore non-letter symbols.

"""

import string
def in_alpha(word):
  nums = list(enumerate(string.ascii_lowercase, 1))
  letters = [i.lower() for i in word if i.isalpha()]
  summ = 0
  for i in letters:
    for a, b in nums:
      if b == i:
        summ += a
  return not summ % 2

