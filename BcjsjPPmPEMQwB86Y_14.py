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
    myans = []
    v = ['a','e','i','o','u']
    for i in range(len(txt)):
        if txt[i] in v:
            for j in range(i,len(txt)):
                if txt[j] in v:
                    if txt[i:j+1] not in myans:
                        myans.append(txt[i:j+1])
    return sorted(myans)
​
def get_consonant_substrings(txt):
    myans = []
    v = ['a','e','i','o','u']
    for i in range(len(txt)):
        if txt[i] not in v:
            for j in range(i,len(txt)):
                if txt[j] not in v:
                    if txt[i:j+1] not in myans:
                        myans.append(txt[i:j+1])
    return sorted(myans)

