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
    # base case
    if len(word) == 0:
        return True
​
    # recursion case
    else:
        if word[0] == word[-1]:
            word = word[1:-1]
            return is_palindrome(word)
​
    return False

