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

vows = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz'
​
def consonants(word):
  c = 0
  for i in word:
    if i.lower() in cons:
      c += 1
  return c
​
def vowels(word):
  v = 0
  for j in word:
    if j.lower() in vows:
      v += 1
  return v

