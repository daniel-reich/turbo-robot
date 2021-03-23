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
  import string
  alphabet = string.ascii_lowercase
  mapping = {}
  num = 1
  for i in alphabet:
    mapping[num] = i
    num +=1
  print(mapping)
  
  idx = len(s)-1 
  decrypt = []
  while idx >=0:
    if s[idx] == '#':
      encode = s[idx-2:idx]
      idx += -3
    else:
      encode = s[idx]
      idx += -1
    decrypt.append(mapping[int(encode)])
  decrypt.reverse()
  return ''.join(decrypt)

