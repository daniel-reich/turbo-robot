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

def is_alpha(word):
  a = ' abcdefghijklmnopqrstuvwxyz'
  return sum([a.index(i) for i in word.lower() if i.isalpha()])%2 == 0

