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
  if not isinstance(num, type(1)) or num < 0:
    return 'invalid'
  res = ""
  for char in word:
    if char.lower() in "aeiouy":
      res += char*(num+1)
    else:
      res += char
  return res

