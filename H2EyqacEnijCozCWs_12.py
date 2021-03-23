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
  l=[x for x in txt if x in "aeiou"]
  return "".join(l[:n]) if n <=len(l) else "invalid"

