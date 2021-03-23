"""


Write a function that returns `True` if it's possible to build a phrase `txt1`
using only the characters from another phrase `txt2`.

### Examples

    can_build("got 2 go", "gogogo 2 today") ➞ True
    
    can_build("sit on top", "its a moo point") ➞ True
    
    can_build("long high add or", "highway road go long") ➞ False
    
    can_build("fill tuck mid", "truck falls dim") ➞ False

### Notes

  * All letters will be in lower case.
  * Numbers and special characters included.
  * Ignore whitespaces.
  * Do not count white space as a character.

"""

import collections
def without_spaces(txt):
  return ''.join(txt.split(" "))
​
def can_build(txt1, txt2):
  txt1 = without_spaces(txt1)
  txt2 = without_spaces(txt2)
  for char in txt1:
    if not char in txt2:
      return False
  t1 = collections.Counter(txt1)
  t2 = collections.Counter(txt2)
  for char in t1.keys():
    if t1[char] > t2[char]:
      return False
  return True

