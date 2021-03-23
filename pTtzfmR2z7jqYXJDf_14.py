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
    c = [0] * 256 
    for i in range( 0, len(txt)) : 
        c[ord(txt[i])] = c[ord(txt[i])] + 1
    odd = 0
    for i in range(0, 256) : 
        if (c[i] & 1) : 
            odd += 1
  
        if (odd > 1) : 
            return False
              
  
    return True

