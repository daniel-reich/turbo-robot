"""


Write a function that returns the first `n` vowels of a string.

### Examples

    first_n_vowels("sharpening skills", 3) ➞ "aei"
    
    first_n_vowels("major league", 5) ➞ "aoeau"
    
    first_n_vowels("hostess", 5) ➞ "invalid"

### Notes

  * Return `"invalid"` if the `n` exceeds the number of vowels in a string.
  * Vowels are: _a, e, i, o, u_

"""

def first_n_vowels(txt, n):
  vowels = ''.join([i for i in txt if i in 'aeiou'])
  return vowels[:n] if len(vowels) >= n else 'invalid'

