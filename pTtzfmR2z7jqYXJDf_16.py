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
    lst = []
    for item in set(txt):
        lst.append(txt.count(item))
    neg = False
    for num in lst:
        if len(txt)%2 == 0 and num%2 != 0 or num%2 != 0 and neg == True:
            return False
        elif num%2 != 0:
            neg = True
    return True

