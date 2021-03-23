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

import re
def is_central(txt):
  spcs = re.findall(r'\s+', txt)
  return len(txt) == 1 or (len(spcs) == 2 and len(spcs[0]) == len(spcs[1]))

