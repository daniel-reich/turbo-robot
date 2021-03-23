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

def consonants(word):
  s=""
  v="aeoui"
  co=0
  for x in word.lower():
    if x.isalpha():
      if x not in v:
        co+=1
  return co
def vowels(word):
  s=""
  v="aeoui"
  vo=0
  for x in word.lower():
    if x.isalpha():
      if x in v:
        vo+=1
  return vo

