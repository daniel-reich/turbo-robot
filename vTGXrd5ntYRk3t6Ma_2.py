"""


An isogram is a word that has no duplicate letters. Create a function that
takes a string and returns either `True` or `False` depending on whether or
not it's an "isogram".

### Examples

    is_isogram("Algorism") ➞ True
    
    is_isogram("PasSword") ➞ False
    # Not case sensitive.
    
    is_isogram("Consecutive") ➞ False

### Notes

  * Ignore letter case (should not be case sensitive).
  * All test cases contain valid one word strings.

"""

def is_isogram(txt):
    word = txt.lower()
    for i in word:
        if word.count(i) > 1:
            return False
    return True

