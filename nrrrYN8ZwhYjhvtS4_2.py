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
  vols = 'aeiouAEIOU'
  new = ''
  if num < 0 or type(num) == float:
    return 'invalid'
  elif num == 0:
    return word
  else:
    for char in word:
      if char not in vols:
        new = new + char
      else:
        new = new + char + (char * num)
    return new

