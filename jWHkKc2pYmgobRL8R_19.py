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
  vwl,ml='aeiou',[]
  for i in range(len(txt)):
    if txt[i] in vwl:
      ml.append(0)
    else:
      counter=1
      while True:   
        if i+counter<len(txt) and txt[i+counter] in vwl or i-counter>=0 and txt[i-counter] in vwl:
          ml.append(counter)
          break
        else:
          counter+=1
  return ml

