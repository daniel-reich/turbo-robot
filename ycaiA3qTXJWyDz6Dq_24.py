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
  counter1 = 0
  vowels = ['a','e','i','o','u']
  not_vowels = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
  for i in word.lower():
    if i in not_vowels:
      counter1 += 1
  return counter1
​
​
​
def vowels(word):
 vowles = ['a','e','i','o','u']
 counter = 0 
 for i in word.lower():
  print(i)
  if i in vowles:
    counter = counter + 1
 return counter
​
print(vowels('Jameel SAEB'))
print(consonants('He|\o mY Fr*end'))

