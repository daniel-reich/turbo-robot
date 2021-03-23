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

def get_all(txt):
  s = [txt[a:b+1] for a in range(len(txt)) for b in range(len(txt)) if txt[a:b+1] != '']
  return sorted(list(set(s)))
​
def get_vowel_substrings(txt):
  return [s for s in get_all(txt) if s[0] in 'aeiou' and s[-1] in 'aeiou']
​
def get_consonant_substrings(txt):
  return [s for s in get_all(txt) if s[0] not in 'aeiou' and s[-1] not in 'aeiou']

