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

from itertools import accumulate
def distance_to_nearest_vowel(txt):
    def dist_to_last(txt):
        normalized = [0 if char in 'aeiou' else 1 for char in txt]
        return list(accumulate([normalized[0]*999]+normalized[1:], lambda a,b: (a+1)*b))
    return [min(to_last, to_next) for to_last, to_next in zip(dist_to_last(txt), reversed(dist_to_last(reversed(txt))))]

