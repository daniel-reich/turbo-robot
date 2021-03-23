"""


Create a function that determines whether it is possible to build a palindrome
from the characters in a string.

### Examples

    possible_palindrome("acabbaa") ➞ True
    # Can make the following palindrome: "aabcbaa"
    
    possible_palindrome("aacbdbc") ➞ True
    # Can make the following palindrome: "abcdcba"
    
    possible_palindrome("aacbdb") ➞ False
    
    possible_palindrome("abacbb") ➞ False

### Notes

N/A

"""

def possible_palindrome(txt):
    t = [txt.count(i) for i in set(txt)]
    if len(set(txt)) == 1:
        return True
    if t.count(1) > 1:
        return False
    return all([False if i % 2 != 0 else True for i in t if i > 1])

