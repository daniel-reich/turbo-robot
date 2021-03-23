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
  txt1 = ""
  txt2 = ""
  for i in txt:
    if i in "eaiouAEIOU":
      txt1 += i
    else:
      txt2+= i
  return txt1+txt2

