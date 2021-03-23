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
    return re.sub(r'\d{2}#|\d',lambda x: chr(96 + int(x.group(0)[:2])) if '#' in x.group(0) else chr(96 + int(x.group(0)[0])),s)

