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

def get_vowel_substrings(txt):
  vowels = 'aeiou'
  res = set()
  for start in range(len(txt)):
    for end in range(start+1,len(txt)+1):
      if txt[start:end][0] in vowels and txt[start:end][-1] in vowels:
        res.add(txt[start:end])
  return sorted([r for r in res])
​
def get_consonant_substrings(txt):
  vowels = 'aeiou'
  res = set()
  for start in range(len(txt)):
    for end in range(start+1,len(txt)+1):
      if txt[start:end][0] not in vowels and txt[start:end][-1] not in vowels:
        res.add(txt[start:end])
  return sorted([r for r in res])

