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
    st = ""
    st1 = ""
    for x in name:
        if x.isalpha():
            st = st+ x.lower()
    st = list(st)
    st.sort()
    st = "".join(st)
    for y in words:
        for a in y:
            st1 = st1 + a.lower()
    st1 = list(st1)
    st1.sort()
    st1 = "".join(st1)
    
    if st == st1:
        return True
    else:
        return False

