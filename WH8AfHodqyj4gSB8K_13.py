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

vowels = "AEIOU"
consonants = ''.join([chr(i) for i in range(65, 91) if chr(i) not in vowels])
​
def is_authentic_skewer(s):
    if s[0] not in consonants or s[-1] not in consonants:
        return False
    idx = s.find('-')
    if idx < 0:
        return False
    cnt = 0
    while idx < len(s) and s[idx] == '-':
        cnt += 1
        idx += 1
    delim = '-' * cnt
    L = s.split(delim)
    for i in range(len(L)):
        c = L[i]
        if len(c) != 1:
            return False
        if i % 2 == 0:
            if c not in consonants:
                return False
        else:
            if c not in vowels:
                return False    
    return True

