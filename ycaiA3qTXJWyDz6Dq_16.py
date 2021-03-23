"""


Make two functions:

  1. `consonants(word)` which returns the number of consonants in a word when called.
  2. `vowels(word)` which returns the number of vowels in a word when called.

### Examples

    vowels('Jameel SAEB') ➞ 5
    
    consonants('He|\o mY Fr*end') ➞ 7
    
    consonants("Smithsonian") ➞ 7
    vowels("Smithsonian") ➞ 4

### Notes

  * Vowels are: `a, e, i, o, u`.
  * Spaces and special character do not count as consonants nor vowels.
  * Check **Resources** for more info.

"""

import re
​
def consonants(word):
    container = 0
    pattern = re.compile('[^AEIOUaieou0-9\s\W]')
    data = pattern.finditer(word)
    for i in data:
        container += 1
​
    return container
​
​
def vowels(word):
​
​
        container = 0
        pattern = re.compile('[AEIOUaieou]')
        data = pattern.finditer(word)
        for i in data:
            container += 1
        return container

