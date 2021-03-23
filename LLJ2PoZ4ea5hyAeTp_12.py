"""
Write a **_DECIMATOR_** function which takes a string and **_decimates_** it
(i.e. it removes the last 1/10 of the characters).

 _Always round up_ : if the string has 21 characters, 1/10 of the characters
would be 2.1 characters, hence the **_DECIMATOR_** removes 3 characters. The
**_DECIMATOR_** shows no mercy!

### Examples

    DECIMATOR("1234567890") ➞ "123456789"
    # 10 characters, removed 1.
    
    DECIMATOR("1234567890AB") ➞ "1234567890"
    # 12 characters, removed 2.
    
    DECIMATOR("123") ➞ "12"
    # 3 characters, removed 1.
    
    DECIMATOR("123456789012345678901") ➞ "123456789012345678"
    # 21 characters, removed 3.

### Notes

Make sure to remove characters from the end of the string.

"""

import math
def DECIMATOR(txt):
  n = len(txt)/10
  n = int(math.ceil(n))
  txt = txt[:-n]
  return txt

