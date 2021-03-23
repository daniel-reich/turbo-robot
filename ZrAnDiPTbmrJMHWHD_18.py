"""


Given a string containing mostly spaces and _one_ non-space character, return
whether the character is positioned in the very centre of the string. This
means the number of spaces on both sides **should be the same**.

### Examples

    is_central("  #  ") ➞ True
    
    is_central(" 2    ") ➞ False
    
    is_central("@") ➞ True

### Notes

Only one character other than spaces will be given at a time.

"""

from re import findall 
def is_central(s):
  if not len(s) % 2:
    return False
  string = '\S'
  x = s.index(findall(string, s)[0])
  length = len(s) // 2
  return length == x

