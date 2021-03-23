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

def is_authentic_skewer(mix):
    '''
    Returns True if mix is a consistent set of vowel - space(s) - consonants
    as per the instructions
    '''
    CONSONANTS = set('BCDFGHJKLMNPQRSTVWXYZ')
    VOWELS = set('AEIOU')
    
    size = len(mix)
    pattern = ''.join(['C' if c in CONSONANTS else 'V' if c in VOWELS else c
                       for c in mix])  # pattern of consonants, vowels etc
    if size < 5 or pattern[0] != 'C' or pattern[1] != '-':
        return False
    
    count = 0
    i = 1
    while pattern[i] == '-':
        count += 1  # size of 1st skewer space
        i += 1
        
    num = size // (2 * (count + 1))  # number of c - v -  sets expected
    legit_set = 'C' + '-' * count + 'V' + '-' * count
    
    return pattern == legit_set * num + 'C'

