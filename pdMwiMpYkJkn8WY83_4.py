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

def is_palindrome(w):
  if len(w) <= 1:
    return True
  elif w[0] == w[-1]:
    return is_palindrome(w[1:-1])
  else:
    return False

