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
  al = 'abcdefghijklmnopqrstuvwxyz'
​
  ans = ''
  idx = 0
  while idx<len(s):
    if idx+2<len(s) and s[idx+2]=='#':
      ans += al[int(s[idx:idx+2])-1]
      idx += 3
    else:
      ans += al[int(s[idx])-1]
      idx += 1
  
  return ans

