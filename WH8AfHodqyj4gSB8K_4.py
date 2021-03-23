"""


An _authentic_ vowel skewer is a skewer with a delicious and juicy mix of
consonants and vowels. However, the way they are made must be _just right_ :

  * Skewers must begin and end with a **consonant**.
  * Skewers must **alternate** between consonants and vowels.
  * There must be an **even spacing** between each letter on the skewer, so that there is a consistent flavour throughout.

Create a function which returns whether a given vowel skewer is **authentic**.

### Examples

    is_authentic_skewer("B--A--N--A--N--A--S") ➞ True
    
    is_authentic_skewer("A--X--E") ➞ False
    # Should start and end with a consonant.
    
    is_authentic_skewer("C-L-A-P") ➞ False
    # Should alternate between consonants and vowels.
    
    is_authentic_skewer("M--A---T-E-S") ➞ False
    # Should have consistent spacing between letters.

### Notes

  * All tests will be given in uppercase.
  * Strings without any actual skewer `"-"` or letters should return `False`.

"""

import re
def is_authentic_skewer(s):
  v = lambda x: x in 'AEIOU'
  sep = re.findall('[^\w]+',s)
  if v(s[0]) == v(s[-1]) == False:
    if len(set(sep)) == 1:
      s = s.split(sep[0])
      if all(len(i)==1 for i in s):
        return all(v(a)!=v(b) for a, b in zip(s,s[1:]))
  return False

