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

def embeded_within(txt, letters):
    return sorted({txt[s:e+1] for e in range(len(txt))
                for s in range(e+1)
                if txt[s] in letters and txt[e] in letters})
​
def get_vowel_substrings(txt):
    return embeded_within(txt, set('aeiou'))
def get_consonant_substrings(txt):
    return embeded_within(txt, set('bcdfghjklmnpqrstvwxyz'))

