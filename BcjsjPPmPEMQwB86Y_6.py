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
  lst = []
  v = 'aeiou'
  for i in range(0,len(txt)):
    for x in range(i+1,len(txt)+1):
      if txt[i:x][0].lower() in v and txt[i:x][-1].lower() in v and txt[i:x] not in lst:
        lst.append(txt[i:x])
  return sorted(lst)
​
def get_consonant_substrings(txt):
  lst = []
  c = 'bcdfghjklmnpqrstvwxyz'
  for i in range(0,len(txt)):
    for x in range(i+1,len(txt)+1):
      if txt[i:x][0].lower() in c and txt[i:x][-1].lower() in c and txt[i:x] not in lst:
        lst.append(txt[i:x])
  return sorted(lst)

