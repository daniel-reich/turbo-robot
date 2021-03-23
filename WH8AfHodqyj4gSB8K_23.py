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
  H=None;E=False;D='-';C='AEIOU'
  if s[0]in C or s[0]==D:return E
  if s[-1]in C or s[-1]==D:return E
  G=0;F=0
  for A in s[1:]:
    if A==D:G+=1
    else:break
  for A in s[1:]:
    if F>G:return E
    elif A!=D:
      if F!=G:return E
      F=0
    elif A==D:F+=1
  B=H
  for A in s:
    if A in C and B==0:return E
    elif A not in C and A!=D and B==1:return E
    elif A in C and(B==1 or B==H):B=0
    elif A not in C and A!=D and(B==0 or B==H):B=1
  return True

