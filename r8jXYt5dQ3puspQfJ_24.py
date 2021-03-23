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
  v = "aeiou"
  txt1 = "".join(i for i in txt if i in v)
  txt2 = "".join(i for i in txt if not i in v)
  return txt1 + txt2

