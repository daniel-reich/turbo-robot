"""


Write a function that returns `True` if a given name can generate an array of
words.

### Examples

    anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True
    
    anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True
    
    anagram("Chris Pratt", ["chirps", "rat"]) ➞ False
    # Not all letters are used
    
    anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False
    # "s" does not exist in the original name

### Notes

  * Each letter in the name may only be used once.
  * All letters in the name must be used.

"""

def anagram(name, words):
    nameDict={}
    wordsDict={}
    name=name.lower()
    for i in name :
        if i in nameDict :
            nameDict[i]+=1
        else:
            nameDict[i]=1
    del nameDict[' ']
    for word in words:
        for j in word:
            if j in wordsDict:
                wordsDict[j] += 1                
            else:
                wordsDict[j] = 1
  
    return nameDict == wordsDict

