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

import re
def split(txt):
  vowelsRegex = re.compile(r'[aeiouAEIOU]')
  consonantsRegex = re.compile(r'[^aeiouAEIOU]')
  vowels = ''.join(vowelsRegex.findall(txt))
  consonants = ''.join(consonantsRegex.findall(txt))
  return vowels + consonants

