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
  letters = [i for i in s if i.isalpha()]
  skewers = ''.join([' ' if i.isalpha() else i for i in s]).split()
  if len(set(skewers))!=1:
    return False
  return len(letters)>=1 and len(skewers)+1==len(letters) and all([letters[i] in 'AEIOU' if i%2==1 else letters[i] not in 'AEIOU' for i in range(len(letters))])

