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

def subs(t,x):
  y = sorted([t[i:j+1] for i in x for j in x if i<=j])
  for i in y:
    if y.count(i) > 1:
      y.remove(i)
  return y
​
def get_vowel_substrings(t):
  v = [i for i in range (len(t)) if t[i] in "aeiou"]
  return subs(t,v)
  
def get_consonant_substrings(t):
  c = [i for i in range (len(t)) if t[i] not in "aeiou"]
  return subs(t,c)

