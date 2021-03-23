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

def is_palindrome(word):
    return len(word)<2 or word[0]==word[-1] and is_palindrome(word[1:-1])

