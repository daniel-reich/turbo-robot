"""


Create a function that takes a `word` and extends all vowels by a number
`num`.

### Examples

    extend_vowels("Hello", 5) ➞ "Heeeeeelloooooo"
    
    extend_vowels("Edabit", 3) ➞ "EEEEdaaaabiiiit"
    
    extend_vowels("Extend", 0) ➞ "Extend"

### Notes

Return `"invalid"` if `num` isn't `0` or a positive integer.

"""

def extend_vowels(word, num):
  new_word = ''
  if num >= 0 and type(num)==int:
    for letter in word:
      new_letter = ''
      if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        for i in range (0, num+1, 1):
          new_letter+=letter
        new_word+=new_letter
      else:
        new_word+=letter
    return new_word
  else:
    return 'invalid'

