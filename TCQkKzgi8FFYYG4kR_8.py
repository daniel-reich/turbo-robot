"""


Create a function that takes a string of words (or just one word) and converts
each word from camelCase to snake_case.

### Examples

    camel_to_snake("magicCarrots") ➞ "magic_carrots"
    
    camel_to_snake("greatApples for aSmellyRhino") ➞ "great_apples for a_smelly_rhino"
    
    camel_to_snake("thatsGreat") ➞ "thats_great"

### Notes

You won't get more than two capitals in a row (e.g. `"DIYFoods"` is not
given).

"""

def camel_to_snake(s):
  def convert(word):
    caps = 'abcdefghijklmnopqrstuvwxyz'.upper()
    new_word = ''
    for l8r in word:
      if l8r in caps:
        new_word += '_' + l8r.lower()
      else:
        new_word += l8r
    return new_word
  
  words = s.split()
  
  return ' '.join(convert(word) for word in words)

