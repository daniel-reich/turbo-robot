"""


Create a function that takes two strings and returns either `True` or `False`
depending on whether they're anagrams or not.

### Examples

    is_anagram("cristian", "Cristina") ➞ True
    
    is_anagram("Dave Barry", "Ray Adverb") ➞ True
    
    is_anagram("Nope", "Note") ➞ False

### Notes

  * Should be case insensitive.
  * The two given strings can be of different lengths.

"""

#edabit
#check anagrams
​
def is_anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    result = True
    if len(text1) != len(text2):
        result = False
    else:
        for t in text1:
            if t not in text2:
                result = False
                break
    return result
​
def main():
    pass
​
if __name__ == "__main__":
    main()

