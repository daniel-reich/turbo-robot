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
    vowels=['a','e','i','o','u']
    position=[]
    place=0
    if len(txt)==0:
        print("No text was submitted.")
    else:
        for i in txt:
            place+=1
            for j in vowels:
                if i==j:
                    position.append(place-1) 
    if len(position)==0:
        print('There were no vowels in submitted text')
    else:
        finalpos=[]
        for i in range(0,len(txt)):
            relpos=[]
            for j in position:
                relpos.append(abs(i-j))
            relpos.sort()
            finalpos.append(relpos[0])
    return finalpos

