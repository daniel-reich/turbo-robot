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
    count = 0
    name = name.lower().replace(" ", "")
    for i in range(len(words)):
        for x in words[i]:
            if words[i].count(x) <= name.count(x):
                count += 1
​
    if count == len(name) and len(set(name)) == len(set("".join(words))):
        return True
    return False

