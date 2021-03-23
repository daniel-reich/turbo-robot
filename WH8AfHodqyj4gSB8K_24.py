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
  a = s.count('-')
  if a == 0:
    return False
  b = s[0]
  c = s[-1]
  d = 0
  vowels = ['A', 'E', 'I', 'O', 'U']
  letters = list(s)
  letters2 = list(s)
  for i in range(a):
    letters.remove('-')
  if b in vowels:
    return False
  elif c in vowels:
    return False
  for i in range(len(letters)):
    if i % 2 != 0:
      if letters[i] not in vowels:
        return False
  for i in range(1, len(letters2)):
    if letters2[i] not in letters:
      d += 1
    else:
      break
  if a % d != 0:
    return False
  else:
    return True

