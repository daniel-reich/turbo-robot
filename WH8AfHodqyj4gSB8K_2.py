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

def is_authentic_skewer(s):
  alpha= [chr(65+i) for i in range (26)]
  vowels='AEIOUaeiou'
  if '-' not in s or not any(c.isalpha() for c in s) or s[0] in vowels or s[-1] in vowels or not s[0].isalpha():
    return False
  consequtive=max_consequtive=0
  for c in s:
    if c=='-':
      consequtive+=1
      if consequtive > max_consequtive:
        max_consequtive = consequtive
    else:
      consequtive =0
  out=''.join(s.split('-'*max_consequtive))
  if not all(c.isalpha() for c in out) :
    return False
  for i in range (len(out)-1):
    if out[i] in vowels:
      if (out[i+1] in vowels):
        return False
    else:
      if not (out[i+1] in vowels):
        return False
  return True

