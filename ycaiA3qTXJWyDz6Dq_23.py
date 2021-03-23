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

from string import ascii_letters
def consonants(word):
  return sum([1 for i in word.lower() if i not in 'aeuio' and i in ascii_letters])
def vowels(word):
  return sum([1 for i in word.lower() if i in 'aeuio' and i in ascii_letters])

