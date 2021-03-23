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
  backwardIndex = -1
  invalidIndexes = []
  almostPalindrome = False
  # Obtain the indexes where the characters are not the same
  for i in range(0, len(txt) // 2):
    if txt[i] != txt[backwardIndex]:
      invalidIndexes.append((i, backwardIndex))
    backwardIndex -= 1
  # Swap the characters where the characters are not the same
  for (startingIndex, backwardIndex) in invalidIndexes:
    chars = list(txt)
    chars[backwardIndex] = chars[startingIndex]
    string = "".join(chars)
    if string == string[::-1]:
      return True
  return almostPalindrome

