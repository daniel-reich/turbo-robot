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

from re import match
def scrambled(words, mask):
    pat = mask.replace("*", r"\w") + "$"
    return [word for word in words if match(pat, word)]

