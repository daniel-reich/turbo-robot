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
  if len(w)<2:return 1
  if w[0]!=w[-1]:return 0
  return is_palindrome(w[1:-1])

