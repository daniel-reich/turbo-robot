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

def distance_to_nearest_vowel(str):
  import numpy as np 
  l=[]
  vow=['a','e','i','o','u']
  for i in range(len(str)):
    if str[i] in vow:
      l.append(0)
    else:
      tmp=[]
      for j in range(len(str)):
        if str[j] in vow:
          tmp.append(j+1)
        else:
          tmp.append(3000)
      for k in range(len(tmp)):
          tmp[k]=np.abs(tmp[k]-(i+1))
      l.append(min(tmp))
  return l

