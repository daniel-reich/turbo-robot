"""


Create a function that accepts a string as an argument and returns the first
non-repeated character.

### Examples

    first_non_repeated_character("g") ➞ "g"
    
    first_non_repeated_character("it was then the frothy word met the round night") ➞ "a"
    
    first_non_repeated_character("the quick brown fox jumps then quickly blows air") ➞ "f"
    
    first_non_repeated_character("hheelloo") ➞ False
    
    first_non_repeated_character("") ➞ False

### Notes

  * An empty string should return `False`.
  * If every character repeats, return `False`.
  * Don't worry about case sensitivity or non-alphanumeric characters.

"""

def first_non_repeated_character(txt):
  if len(txt) == 0: return False
  txt = txt.lower()
  cnt = {}
  for c in txt:
    if c in cnt:
      cnt[c] += 1
    else:
      cnt[c] = 1
  for c in txt:
    if cnt[c] == 1:
      return c
  return False

