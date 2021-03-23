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

vowels = ["a", "e", "i", "o", "u"]
​
def distance_to_nearest_vowel(txt):
  res = []
  vow = []
  for i in range(len(txt)):
    c = txt[i]
    res.append(0 if c in vowels else -1)
    if c in vowels: vow.append(i)
  for i in range(len(res)):
    if res[i] == -1:
      min = float("inf")
      for v in vow:
        if abs(i - v) < min:
          min = abs(i - v)
      res[i] = min
  return res

