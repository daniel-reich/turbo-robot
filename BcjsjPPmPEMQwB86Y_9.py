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

CONS = 'bcdfghjklmnpqrstvwxyz'
VOWS = 'aeiou'
​
is_consub = lambda x: x[0] in CONS and x[-1] in CONS
is_vowsub = lambda x: x[0] in VOWS and x[-1] in VOWS
​
def get_subs(word, f):
    '''
    Uses function f to decide whether to search for consonant or vowel
    substrings then returns the unique ones in sorted order as per the
    instructions.
    '''
    return sorted(set([word[i:j] for i in range(len(word)) \
                       for j in range(i+1, len(word)+1) if f(word[i:j])]))
​
def get_vowel_substrings(word):
    '''
    Returns a sorted set of vowel substrings as per the instructions.
    '''
    return get_subs(word, is_vowsub)
​
def get_consonant_substrings(word):
    '''
    Returns a sorted set of consonant substrings as per the instructions.
    '''
    return get_subs(word, is_consub)

