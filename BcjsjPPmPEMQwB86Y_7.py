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
    vowels = [(i, txt[i]) for i in range(len(txt)) if txt[i] in {'a', 'e', 'o', 'i', 'u'}]
    substring = set()
    for i in range(len(vowels)):
        for j in range(len(vowels)):
            sub = txt[vowels[i][0] : (vowels[j][0]) + 1]
            if sub:
                substring.add(sub)  
    substring |= set(i[1] for i in vowels)
    return sorted(list(substring))
​
def get_consonant_substrings(txt):
    consonant = [(i, txt[i]) for i in range(len(txt)) if txt[i] not in {'a', 'e', 'o', 'i', 'u'}]
    substring = set()
    for i in range(len(consonant)):
        for j in range(len(consonant)):
            sub = txt[consonant[i][0] : (consonant[j][0]) + 1]
            if sub:
                substring.add(sub)                 
    substring |= set(i[1] for i in consonant)
    return sorted(list(substring))

