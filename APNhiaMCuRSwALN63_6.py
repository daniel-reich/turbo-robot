"""


A string is an **almost-palindrome** if, by changing **only one character** ,
you can make it a palindrome. Create a function that returns `True` if a
string is an **almost-palindrome** and `False` otherwise.

### Examples

    almost_palindrome("abcdcbg") ➞ True
    # Transformed to "abcdcba" by changing "g" to "a".
    
    almost_palindrome("abccia") ➞ True
    # Transformed to "abccba" by changing "i" to "b".
    
    almost_palindrome("abcdaaa") ➞ False
    # Can't be transformed to a palindrome in exactly 1 turn.
    
    almost_palindrome("1234312") ➞ False

### Notes

Return `False` if the string is already a palindrome.

"""

def almost_palindrome(txt):
  l = len(txt)//2
  if l % 2:
    return sum(1 for x, y in zip(txt[l+1:][::-1], txt[:l]) if x != y) == 1
  return sum(1 for x, y in zip(txt[l:][::-1], txt[:l]) if x != y) == 1

