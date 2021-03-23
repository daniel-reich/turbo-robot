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
  vowels = "aeiou"
  lst = []
  str = ""
  for i in range(len(txt)):
    str = txt[i]
    if txt[i] in vowels:
      lst.append(txt[i])
      for j in txt[i+1:]:
        str += j
        if j in vowels:
          lst.append(str)
  return sorted(set(lst))
​
def get_consonant_substrings(txt):
  consonants = "bcdfghjklmnpqrstvwxyz"
  lst = []
  str = ""
  for i in range(len(txt)):
    str = txt[i]
    if txt[i] in consonants:
      lst.append(txt[i])
      for j in txt[i+1:]:
        str += j
        if j in consonants:
          lst.append(str)
  return sorted(set(lst))

