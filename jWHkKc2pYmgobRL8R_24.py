"""


Write a function that takes in a string and for each character, returns the
distance to the nearest vowel in the string. If the character is a vowel
itself, return `0`.

### Examples

    distance_to_nearest_vowel("aaaaa") ➞ [0, 0, 0, 0, 0]
    
    distance_to_nearest_vowel("babbb") ➞ [1, 0, 1, 2, 3]
    
    distance_to_nearest_vowel("abcdabcd") ➞ [0, 1, 2, 1, 0, 1, 2, 3]
    
    distance_to_nearest_vowel("shopper") ➞ [2, 1, 0, 1, 1, 0, 1]

### Notes

  * All input strings will contain **at least one vowel**.
  * Strings will be lowercased.
  * Vowels are: `a, e, i, o, u`.

"""

def distance_to_nearest_vowel(txt):
  
  return [distance(i, s, txt) for i, s in enumerate(txt)]
  
def distance(i, s, txt):
  vowels = ("a", "e", "i", "u", "o")
  d = 0
  if s in vowels:
    return d
​
  d = len(txt)
  
  if i > 0:
    for j, _s in enumerate(txt[:i][::-1]):
      if _s in vowels:
        d = j+1
        break
  if i < len(txt):
    for j, _s in enumerate(txt[i:]):
      if _s in vowels:
        d = j if j < d else d
        break 
  return d

