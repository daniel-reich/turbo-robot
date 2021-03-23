"""


A palindrome is a word that is identical forward and backwards.

  * mom
  * racecar
  * kayak

Given a word, create a function that checks whether it is a palindrome.

### Examples

    is_palindrome("mom") ➞ True
    
    is_palindrome("scary") ➞ False
    
    is_palindrome("reviver") ➞ True
    
    is_palindrome("stressed") ➞ False

### Notes

All test input is lower cased.

"""

def is_palindrome(txt):
  new = []
  for char in txt:
    new.append(char)
  
  if "".join(new[::-1]) == txt:
    return True
  else:
    return False

