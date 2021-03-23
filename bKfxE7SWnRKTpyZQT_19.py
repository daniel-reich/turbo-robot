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

def replace_vowel(word):
    if 'a' in word:
        word=word.replace('a','1')
    if 'e' in word:
        word=word.replace('e','2')
    if 'i' in word:
        word=word.replace('i','3')
    if 'o' in word:
        word=word.replace('o','4')
    if 'u' in word:
        word=word.replace('u','5')
    return word

