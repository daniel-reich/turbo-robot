"""


Write a function that takes a string, breaks it up and returns it with vowels
first, consonants second. For any character that's not a vowel (like special
characters or spaces), treat them like consonants.

### Examples

    split("abcde") ➞ "aebcd"
    
    split("Hello!") ➞ "eoHll!"
    
    split("What's the time?") ➞ "aeieWht's th tm?"

### Notes

  * Vowels are `a, e, i, o, u`.
  * Define a separate `is_vowel()` function for easier to read code (recommendation).

"""

def split(txt):
  def is_vowel(c):
    if c in ['a','e','i','o','u']:
      return True
    else: 
      return False
  vStr = ""
  nvStr = ""
  for i in txt:
    if is_vowel(i):
      vStr += i
    else:
      nvStr += i
  return vStr+nvStr

