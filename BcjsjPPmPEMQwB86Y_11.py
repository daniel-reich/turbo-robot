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

vowels = ["a","e","i","o","u"]
​
def get_vowel_substrings(txt):
  substrings = []
  for i in range(len(txt)):
    for j in range(len(txt)):
      if j<i: 
        continue
      elif txt[i] in vowels and txt[j] in vowels:
        if txt[i:j+1] not in substrings:
          substrings.append(txt[i:j+1])
  return sorted(substrings)
​
def get_consonant_substrings(txt):
  substrings = []
  for i in range(len(txt)):
    for j in range(len(txt)):
      if j<i: 
        continue
      elif txt[i] not in vowels and txt[j] not in vowels:
        if txt[i:j+1] not in substrings:
          substrings.append(txt[i:j+1])
  return sorted(substrings)

