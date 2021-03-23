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
  h = [i for i, n in enumerate(s) if n=='#']
  conv = lambda x: chr(int(x)+96)
  is_2d = lambda i: i+1 in h or i+2 in h
  dc = [conv(s[i-2:i]) if x=='#' else conv(x)
        for i, x in enumerate(s) if x=='#' or not is_2d(i)]
  return ''.join(dc)

