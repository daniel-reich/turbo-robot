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
  txt_rev = txt[::-1]
  different = filter(lambda x: x[0] != x[1], zip(txt, txt_rev))
  return len(list(different)) == 2
  
print(almost_palindrome('meetsysteea'))

