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

import re
​
def extend_vowels(word, num):
  return re.sub(
    '[aeiouAEIOU]', 
    lambda x: (num + 1) * x.group(), 
    word
  ) if not num % 1 and num >= 0 else 'invalid'

