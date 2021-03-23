"""


Write a function that **recursively** determines if a string is a palindrome.

### Examples

    is_palindrome("abcba") ➞ True
    
    is_palindrome("b") ➞ True
    
    is_palindrome("") ➞ True
    
    is_palindrome("ad") ➞ False

### Notes

An empty string counts as a palindrome.

"""

def is_palindrome(txt) :
    for i in range(int((len(txt)/2))):
        if txt[i] == txt[len(txt)-i-1] :
            continue
        else:
            return False
    return True

