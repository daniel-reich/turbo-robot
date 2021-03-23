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

vowels = ['a', 'e', 'i', 'o', 'u']
def get_vowel_substrings(txt):
  global vowels
  return sorted(set([txt[i: j + 1] for j in range(len(txt)) for i in range(j + 1) if txt[i] in vowels
      if txt[j] in vowels]))
​
def get_consonant_substrings(txt):
  global vowels
  return sorted(set([txt[i: j + 1] for j in range(len(txt)) for i in range(j + 1) if txt[i] not in vowels if txt[j]
      not in vowels]))

