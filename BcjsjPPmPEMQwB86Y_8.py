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

def is_vowel(l8r):
  vowels = 'aeiou' + 'AEIOU'
  return l8r in vowels
​
def get_vowel_substrings(txt):
  groups = []
​
  for n in range(len(txt)):
    l8r = txt[n]
    if is_vowel(l8r) == True:
      groups.append(l8r)
      for num in range(n+1, len(txt)):
        tl8r = txt[num]
        if is_vowel(tl8r) == True:
          groups.append(txt[n:num+1])
  
  return sorted(list(set(groups)))
​
def get_consonant_substrings(txt):
  groups = []
​
  for n in range(len(txt)):
    l8r = txt[n]
    if is_vowel(l8r) == False:
      groups.append(l8r)
      for num in range(n+1, len(txt)):
        tl8r = txt[num]
        if is_vowel(tl8r) == False:
          groups.append(txt[n:num+1])
  
  return sorted(list(set(groups)))

