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
  vowels = "aeiouAEIOU"
  txt = ""
  if type(num) != int or num < 0:
    return "invalid"
  for i in word:
    if i in vowels:
      w = 0
      while w <= num:
        txt += i
        w += 1
    else:
      txt += i
  return txt

