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
    vows = 'AOUIE'
    for c in (s[0], s[-1]):
        if c in vows or c == '-':
            return False
    sep_len = 0
    i = 1
    while i < len(s) and s[i] == '-':
        sep_len += 1
        i += 1
    if i == len(s):
        return False
    if sep_len == 0:
        return False
    if s[i] not in vows:
        return False
    last_cons = False
    sep = '-' * sep_len
    i += 1
    while i + sep_len < len(s):
        if s[i:i+sep_len] != sep:
            return False
        if s[i+sep_len] == '-' or (s[i+sep_len] in vows) != last_cons:
            return False
        i += sep_len + 1
        last_cons = not last_cons
    return i == len(s)

