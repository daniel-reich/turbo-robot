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
    sov = set()
    for i, x in enumerate(txt):
        if x in 'aeiou':
            for j in range(i, len(txt)):
                if txt[j] in 'aeiou':
                    sov.add(txt[i:j+1])
    return sorted(sov)
                              
def get_consonant_substrings(txt):
    soc = set()
    for i, x in enumerate(txt):
        if x not in 'aeiou':
            for j in range(i, len(txt)):
                if txt[j] not in 'aeiou':
                    soc.add(txt[i:j+1])
    return sorted(soc)

