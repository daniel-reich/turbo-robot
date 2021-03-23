"""


A palindrome is a series of letters or numbers that reads equivocally
backwards. Write a **recursive** function that determines whether a given
string is a **palindrome** or not.

### Examples

    is_palindrome("Go hang a salami, I'm a lasagna hog!") ➞ True
    
    is_palindrome("This phrase, surely, is not a palindrome!") ➞ False
    
    is_palindrome("Eva, can I see bees in a cave?") ➞ True

### Notes

  * Symbols and special characters should be ignored.
  * You are expected to solve this challenge via **recursion**.
  * You can check on the **Resources** tab for more details about _recursion_.

"""

def is_palindrome(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Forwards = ""
    Parameters.append(Forwards)
    Backwards = ""
    Parameters.append(Backwards)
    
  Sample = Parameters[0].lower()
  Forwards = Parameters[1]
  Backwards = Parameters[2]
  
  if (Sample == "") and (Forwards == Backwards):
    return True
  elif (Sample == "") and (Forwards != Backwards):
    return False
  elif (Sample[0].isalpha()):
    Forwards = Forwards + Sample[0]
    Backwards = Sample[0] + Backwards
    return is_palindrome(Sample[1:], Forwards, Backwards)
  else:
    return is_palindrome(Sample[1:], Forwards, Backwards)

