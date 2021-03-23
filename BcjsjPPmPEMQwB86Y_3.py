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
  vowels = ["a", "e", "i", "o", "u"]
  result = []
  for letter in range(len(txt)):
    if txt[letter] in vowels:
      for letter2 in range(letter, len(txt)):
        if txt[letter2] in vowels:
          res = txt[letter : letter2 + 1]
          if res not in result:
            result.append(res)
  return sorted(result)
​
def get_consonant_substrings(txt):
  vowels = ["a", "e", "i", "o", "u"]
  result = []
  for letter in range(len(txt)):
    if txt[letter] not in vowels:
      for letter2 in range(letter, len(txt)):
        if txt[letter2] not in vowels:
          res = txt[letter : letter2 + 1]
          if res not in result:
            result.append(res)
  return sorted(result)

