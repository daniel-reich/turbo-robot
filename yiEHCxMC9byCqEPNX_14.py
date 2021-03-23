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

from string import ascii_lowercase as al
def is_palindrome(p):
  sanitize = ""
  for letter in p.lower():
    if letter in al:
      sanitize += letter
  if len(sanitize) < 2:
    return True
  return sanitize[0] == sanitize[-1] and is_palindrome(sanitize[1:-1])

