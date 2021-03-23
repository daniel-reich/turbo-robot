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
  
  # Establishing Unique Letters
  
  Sample = str(txt)
  SL = len(Sample)
  
  Unique = []
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Letter = Sample[Counter]
    
    if (Letter in Unique):
      Counter += 1
    else:
      Unique.append(Letter)
      Counter += 1
  
  # Establishing Frequencies of Unique Letters
  
  Sample = str(txt)
  
  Evens = []
  Odds = []
  
  Counter = 0
  Length = len(Unique)
  
  while (Counter < Length):
    Letter = Unique[Counter]
    Occurrences = Sample.count(Letter)
    
    if (Occurrences % 2 == 0):
      Evens.append(Letter)
      Counter += 1
    else:
      Odds.append(Letter)
      Counter += 1
  
  # Establishing Viability of Palindrome
  
  SL = len(Sample)
  OL = len(Odds)
  EL = len(Evens)
  
  if (SL % 2 == 0) and (OL == 0):
    return True
  elif (SL % 2 != 0) and (OL == 1):
    return True
  else:
    return False

