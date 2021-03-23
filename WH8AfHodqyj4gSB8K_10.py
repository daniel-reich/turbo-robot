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
    vowels = list('AEIOU')
    if s[0] == '-':
        return False
  
    #  check if spacing is consistent
    letters = [x for x in s if x.isalpha()]
    d = (s.index(letters[1]) - 1) * '-'
    if not d:
        return False
    if s.split(d) != letters:
        return False
    
    if letters[0] in vowels and letters[-1] in vowels:
        return False
​
    if set(letters[1::2]).difference(vowels):
        return False
    
    if any(x in vowels for x in letters[::2]):
        return False
    
    return True

