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

from itertools import combinations
​
def get_vowel_substrings(txt):
  res = [i for i in txt if i in 'aeiou']
  positions = [idx for idx, i in enumerate(txt) if i in 'aeiou']
  
  for a, b in combinations(positions, 2):
    if txt[b] in 'aeiou':
      res.append(txt[a: b+1])
  return sorted(set(res)) 
​
def get_consonant_substrings(txt):
  res = [i for i in txt if i not in 'aeiou']
  positions = [idx for idx, i in enumerate(txt) if i not in 'aeiou']
  
  for a, b in combinations(positions, 2):
    if txt[b] not in 'aeiou':
      res.append(txt[a: b+1])
  return sorted(set(res))

