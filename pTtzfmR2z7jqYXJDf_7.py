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
  oneOdd = False
  if len(set(txt)) == 1:
    return True
  if len(txt) %2:
    for letter in txt:
      if txt.count(letter) % 2:
        if oneOdd == True:
          return False
        else:
          oneOdd = True
  else:
    for letter in txt:
      if txt.count(letter) % 2:
        return False
  
  return True

