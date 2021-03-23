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

def s_iter(s):
  it = reversed(s)
  while True:
    c = next(it, None)
    if c is None:
      return
    elif c == '#':
      yield int(next(it)) + 10 * int(next(it))
    else:
      yield int(c) 
​
def decrypt(s):
  msg = [chr(96 + x) for x in s_iter(s)]
  return ''.join(reversed(msg))

