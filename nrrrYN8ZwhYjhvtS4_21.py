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
  if type(num) == float or num < 0:
    return "invalid"
  result = ""
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  for char in word:
    if char in vowels:
      result += (char*(num+1))
    else:
      result += char
  return result

