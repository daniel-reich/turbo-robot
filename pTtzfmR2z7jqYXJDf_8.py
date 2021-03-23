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
    result = sum(filter(lambda x: x%2==1, [txt.count(i) for i in set(txt)]))
    if len(set(txt))==len(txt):
        return False
    else:
        return result == 0 or result%2 == 1

