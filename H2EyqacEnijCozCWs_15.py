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
  mystr = ''
  vowels = ['a','e','i','o','u']
  for i in range (len(txt)):
    if txt[i] in vowels and n>0:
      mystr += txt[i]
      n -= 1
  if (n>0):
    return "invalid"
  return mystr

