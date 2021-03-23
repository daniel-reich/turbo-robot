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
  vwls = 'aeiou' + 'aeiou'.upper()
  print([i for i in word if i not in vwls and i.isalpha()])
  return len([i for i in word if i not in vwls and i.isalpha()])
​
def vowels(word):
  vwls = 'aeiou' + 'aeiou'.upper()
  return len([i for i in word if i in vwls])

