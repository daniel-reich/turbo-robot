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
    vowels = 'aeiou'
    res = []
    for idx, char in enumerate(txt):
        if char in vowels:
            res.append(0)
        else:
            forward = backward = 1000
            for x in range(1, len(txt) - idx):
                if txt[idx + x] in vowels:
                    forward = x
                    break
            for y in range(0, idx + 1 ):
                if txt[idx - y] in vowels:
                    backward = y
                    break
            if forward < backward:
                res.append(forward)
            else:
                res.append(backward)
    return res

