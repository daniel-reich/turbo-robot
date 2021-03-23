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
    parsed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
​
    indexs = [i for i , word in enumerate(txt) if word in vowels]
​
    for idx , letter in enumerate(txt):
      closest = min([abs(x - idx) for x in indexs])
      parsed.append(closest)
​
    return parsed

