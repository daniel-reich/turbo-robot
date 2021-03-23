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

def distance_to_nearest_vowel(string):
    string = [0 if letter in ['a', 'e', 'i', 'o', 'u'] else 1 for letter in list(string) ]
    for index in range(len(string)):
        letter = string[index] 
        if letter == 1:
            current_min = len(string)
            for index2 in range(len(string)):
                if string[index2] == 0: 
                    if abs(index2 - index) < current_min:
                        current_min = abs(index2 - index)
            string[index] = current_min
    return string

