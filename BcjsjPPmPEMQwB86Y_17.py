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

def get_vowel_substrings(string):
  solution = []
  vowels = ['a','e','i','o','u']
  for num in range(len(string)):
    for digit in range(num+1, len(string)+1):
      if string[num:digit][0] in vowels and string[num:digit][-1] in vowels:
        solution.append(string[num:digit])
  return sorted(set(solution))
​
def get_consonant_substrings(string):
  solution = []
  consonants = [
  'b','c','d','f','g','h','j',
  'k','l','m','n','p','q','r','s','t','v','x','z','w','y'
      ]
  for num in range(len(string)):
    for digit in range(num+1, len(string)+1):
      if string[num:digit][0] in consonants and string[num:digit][-1] in consonants:
        solution.append(string[num:digit])
  return sorted(set(solution))

