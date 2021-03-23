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

def distance_to_nearest_vowel(x):
  vowels=['a','e','i','o','u']
  positions=[]
  for element in range(len(x)):
    if x[element] in vowels:
      positions.append(element)
  final=[]
  for element1 in range(len(x)):
    if x[element1] in vowels:
      final.append(0)
    if x[element1] not in vowels:
      minimum=len(x)
      for element2 in positions:
        if element1-element2<0:
          y=-(element1-element2)
          if y<minimum:
            minimum=y
        if element1-element2>0:
          y=(element1-element2)
          if y<minimum:
            minimum=y
      final.append(minimum)
  return final

