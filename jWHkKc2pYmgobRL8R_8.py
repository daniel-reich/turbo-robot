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
    vov = ['a', 'e', 'i', 'o', 'u']
​
    distanceList = []
​
    for i, char in enumerate(txt):
        if(char in vov):
            distanceList.append(0)
            for j in range(i-1,-1,-1):
                if(0 not in distanceList[0:i]):
                    distanceList[j] = i-j
                else:
                    if(distanceList[j] > i-j):
                        distanceList[j] = i-j
        else:
            if(len(distanceList) == 0):
                distanceList.append(1)
            else:
                distanceList.append(distanceList[-1] + 1)
​
    return distanceList

