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

def is_palindrome(p):
  p = "".join([let.lower() for let in p if let.isalpha()])
  if len(p) < 2:
    return True
  if p[0] != p[-1]:
    return False
  return is_palindrome(p[1:-1])

