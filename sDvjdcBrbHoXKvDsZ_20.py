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
    name = name.replace(' ', '')
    name = list(name.lower())
    words = [tuple(i) for i in words]
    for word in words:
        word_letters_in_name = []
        for word_letter in word:
            if word_letter in name:
                word_letters_in_name += word_letter
                if len(word_letters_in_name) == len(word):
                    for j in word:
                        name.remove(j)
    if len(name) == 0:
        return True
    else:
        return False

