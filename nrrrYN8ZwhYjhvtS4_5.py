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
  print(num)
  print(word)
  voyelle=["a", "e", "i", "o", "u", "y"]
  wordfinal=""
  if type(num)==int and num>=0:
    for i in range(len(word)):
      letter=word[i]
      if letter in voyelle or letter.lower() in voyelle:
        wordfinal+=letter*(num+1)
      else:
        wordfinal+=letter
  else:
    wordfinal="invalid"
  return wordfinal

