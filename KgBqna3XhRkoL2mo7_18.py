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
  s = list(s)
  while any(i == "#" for i in s):
    tag = s.index("#")
    s[tag - 2:tag] = ["".join(s[tag - 2:tag])]
    del s[tag - 1]
  return "".join(chr(96 + int(i)) for i in s)

