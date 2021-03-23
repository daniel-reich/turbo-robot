"""


Create a function that takes a word and returns `True` if the word has two
consecutive identical letters.

### Examples

    double_letters("loop") ➞ True
    
    double_letters("yummy") ➞ True
    
    double_letters("orange") ➞ False
    
    double_letters("munchkin") ➞ False

### Notes

N/A

"""

def double_letters(word):
        dub = False
        for i in range(0, len(word)-1):
                if word[i] == word[i+1]:
                        dub = True
                        break
        return dub

