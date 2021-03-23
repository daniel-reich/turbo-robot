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

vowels = "a e i o u".split()
​
def distance_to_nearest_vowel(txt):
​
  
  list = []
  
  for idx, l in enumerate(txt):
  
    if l in vowels:
      list.append(0)
    else:
      forward = txt[idx+1:]
      backward = txt[0:idx][::-1]
      #forward = txt[idx+1:]
      #backward = txt[0:idx][::-1]
      
      f_first = first_vowel(forward)
      b_first = first_vowel(backward)
      
      list.append(min(f_first,b_first)+1)
    
  return list
​
def first_vowel(word):
  for i, l in enumerate(word):
    if l in vowels:
      return i
      
  return 1000000

