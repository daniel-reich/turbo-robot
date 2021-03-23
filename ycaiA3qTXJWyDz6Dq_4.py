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
    consonants = 'qwrtypsdfghjklzxcvbnm'
    consonant_count = 0
​
    for letter in word:
        if letter.lower() in consonants:
            consonant_count += 1
​
    return consonant_count
  
​
def vowels(word):
    vowels = 'aeiou'
    vowel_count = 0
​
    for letter in word:
        if letter.lower() in vowels:
            vowel_count += 1
​
    return vowel_count

