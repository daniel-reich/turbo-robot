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

vows = 'aeiou'
​
def get_vowel_substrings (txt):
  n = []
  i = 0
  for t in txt:
    if t in vows: n.append (i)
    i += 1
  a = [(i,j) for i in n for j in n if j >= i]
  return (sorted (set([txt[i[0]:i[1]+1] for i in a])))
​
def get_consonant_substrings (txt):
  n = []
  i = 0
  for t in txt:
    if t not in vows: n.append (i)
    i += 1
  a = [(i,j) for i in n for j in n if j >= i]
  return (sorted (set([txt[i[0]:i[1]+1] for i in a])))

