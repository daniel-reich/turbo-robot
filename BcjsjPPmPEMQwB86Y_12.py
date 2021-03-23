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
    vowels = 'aeiou'.strip(' ')
    if len(txt) == 1: 
        return [txt] if txt in vowels else []
​
    substrings = []
    for v,_ in enumerate(txt):
        if _ in vowels:
            substrings.append(_)
        else:
            continue
        if len(txt) == v+1:
            break
​
        for vmore,__ in enumerate(txt[v+1:]):
            if __ in vowels:
                substrings.append(''.join(txt[v:vmore+v+2]))
            else:
                continue
​
    substrings = list(set(substrings))
​
    if substrings.count('') :substrings.remove('')
    substrings = sorted(substrings)
    return substrings
​
​
​
def get_consonant_substrings(txt):
    consonants = ''.join(set('abcdefghijklmnopqrstuvwxyz') - set('aeiou'))
    if len(txt) == 1:
        return [txt] if txt in consonants else []
    substrings = []
    
    for v,_ in enumerate(txt):
        if _ in consonants:
            substrings.append(_)
        else:
            continue
        if len(txt) == v+1:
            break
        for vmore, __ in enumerate(txt[v+1:]):
            if __ in consonants:
                substrings.append(''.join(txt[v:vmore+v+2]))
            else:
                continue
    substrings = list(set(substrings))
    if substrings.count('') : substrings.remove('')
    substrings = sorted(substrings)
    return substrings

