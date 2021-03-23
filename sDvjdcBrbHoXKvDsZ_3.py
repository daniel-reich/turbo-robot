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

from collections import Counter
def anagram(str1, lst):
    cc = Counter(str1.replace(" ", '').lower())
    cc2 = Counter(''.join(lst).replace(" ", '').lower())
    if len(cc2) == len(cc):
        if sorted([(k, v) for k, v in cc2.items()]) == sorted([(k1, v1) for k1, v1 in cc.items()]):
            return True
        else:
            return False
    else:
        return False

