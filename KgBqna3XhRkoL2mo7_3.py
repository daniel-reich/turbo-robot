"""


Given a string `s` consisting from digits and `#`, translate `s` to English
lowercase characters as follows:

  * Characters ("a" to "i") are represented by ("1" to "9").
  * Characters ("j" to "z") are represented by ("10#" to "26#").

### Examples

    decrypt("10#11#12") ➞ "jkab"
    
    decrypt("1326#") ➞ "acz"
    
    decrypt("25#") ➞ "y"

### Notes

N/A

"""

def decrypt(s):
  i,res = len(s)-1,''
  while i >= 0:
    if s[i] == '#':
      res = chr(int(s[i-2:i])+96) + res
      i -= 3
    else:
      res = chr(int(s[i])+96) + res
      i -= 1
  return res

