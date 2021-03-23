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

import itertools
​
def get_vowel_substrings(txt):
  found_singles = [x[0] for x in enumerate(txt) if x[1] in 'aeiou']
  found_pairs = list(itertools.combinations(found_singles, 2))
  out = [txt[x] for x in found_singles]
  out.extend([txt[x[0]:x[1] + 1] for x in found_pairs])
  return sorted(set(out))
​
def get_consonant_substrings(txt):
  found_singles = [x[0] for x in enumerate(txt) if x[1] not in 'aeiou']
  found_pairs = list(itertools.combinations(found_singles, 2))
  out = [txt[x] for x in found_singles]
  out.extend([txt[x[0]:x[1] + 1] for x in found_pairs])
  return sorted(set(out))

