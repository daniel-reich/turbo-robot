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

from string import ascii_letters
​
def is_palindrome(p):
  # clean up the string (we may be doing it again)
  p = "".join([c for c in p if c in ascii_letters]).lower()
  # an empty string or a single character is a palindrome 
  if len(p) < 2:
    return True
  # if first and last don't match, return False
  if p[0] != p[-1]:
    return False
  # otherwise, check the middle
  return is_palindrome(p[1:-1])

