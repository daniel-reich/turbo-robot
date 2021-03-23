"""


Write two functions:

  1. One to retrieve all **unique** substrings that **start** and **end** with a **vowel**.
  2. One to retrieve all **unique** substrings that **start** and **end** with a **consonant**.

The resulting array should be sorted in lexicographic ascending order (same
order as a dictionary).

### Examples

    get_vowel_substrings("apple")
    ➞ ["a", "apple", "e"]
    
    get_vowel_substrings("hmm") ➞ []
    
    get_consonant_substrings("aviation")
    ➞ ["n", "t", "tion", "v", "viat", "viation"]
    
    get_consonant_substrings("motor")
    ➞ ["m", "mot", "motor", "r", "t", "tor"]

### Notes

  * Remember the output array should have **unique** values.
  * The word itself counts as a potential substring.
  * Exclude the empty string when outputting the array.

"""

cons = "bcdfghjklmnpqrstvwxyz"
def slicer(w):
  l = len(w)
  return {w[i:i+s] for s in range(1,l+1) for i in range(l-s+1)}
​
def get_vowel_substrings(txt):
  return sorted(x for x in slicer(txt) if x[0] in "aeiou" and x[-1] in "aeiou")
​
def get_consonant_substrings(txt):
  return sorted(x for x in slicer(txt) if x[0] in cons and x[-1] in cons)

