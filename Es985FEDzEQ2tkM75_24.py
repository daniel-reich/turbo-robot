"""


Create a function that takes two arguments (`text`, `key`) and returns a new
encrypted text using the `key`. For example, if the input is `"a"` and the key
is `1`, it should move that letter 1 step in alphabetic order so the output
would be `"b"`.

### Examples

    caesar_cipher("hello", 5) ➞ "mjqqt"
    
    caesar_cipher("hello world", 1) ➞ "ifmmp xpsme"
    
    caesar_cipher("a", 2) ➞ "c"

### Notes

The input is only letters and spaces; no special characters.

"""

import string
import re
def caesar_cipher(s, k):
  newS = "" 
  for i in range(len(s)):  
    val = ord(s[i])  
    dup = k  
    if val + k>122:  
      k -= (122-val)
      k = k % 26
      newS += chr(96 + k)  
    else:
      newS += chr(val + k)  
    k = dup
  chars = re.escape(string.punctuation)
  return re.sub(r'['+chars+']', ' ',newS)

