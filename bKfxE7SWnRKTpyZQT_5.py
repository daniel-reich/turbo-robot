"""


Create a function that takes a string and replaces the vowels with another
character.

  * a = 1
  * e = 2
  * i = 3
  * o = 4
  * u = 5

### Examples

    replace_vowel("karachi") ➞ "k1r1ch3"
    
    replace_vowel("chembur") ➞ "ch2mb5r"
    
    replace_vowel("khandbari") ➞ "kh1ndb1ri"

### Notes

The input will always be in lowercase.

"""

abc = {
  'a': '1',
  'e': '2',
  'i': '3',
  'o': '4',
  'u': '5'
}
​
def replace_vowel(word):
  return ''.join( [ abc[l] if l in 'aeiou' else l for l in word ] )

