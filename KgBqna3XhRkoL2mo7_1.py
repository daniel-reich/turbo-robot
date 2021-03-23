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

import re
def decrypt(s):
  for x in re.findall('..#',s):s=s.replace(x,chr(int(x[:-1])+96))
  return s.translate(s.maketrans('123456789','abcdefghi'))

