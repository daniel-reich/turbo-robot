"""


Write a function that receives a list of words and a mask. Return a list of
words, sorted alphabetically, that match the given mask.

### Examples

    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “*re**”) ➞ [“creed”]
    
    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “***”) ➞ [“dee”, “ree”]

### Notes

The length of a mask will never exceed the length of the longest word in the
word list.

"""

def check(word, mask):
    if len(word) != len(mask):
        return False
    for i in range(len(word)):
        if mask[i] != '*' and mask[i] != word[i]:
            return False
    return True
    
def scrambled(words, mask):
    return sorted([word for word in words if check(word, mask)])

